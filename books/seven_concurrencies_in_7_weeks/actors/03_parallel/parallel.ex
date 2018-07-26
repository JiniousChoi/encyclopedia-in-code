defmodule Parallel do
  def map(collection, fun) do
    parent = self()

    # processes := pids
    pids = Enum.map(collection, fn(e) ->
      spawn_link(fn() -> 
        IO.puts("message #{e} received")
        send(parent, {self(), fun.(e)});
        IO.puts("message #{e} sent")
      end)
    end)
    # Enum.map executes function `fn` for each element in collection
    # In this case, it spawns processes for each element
    # process of which executes callback fn, which sends result of fun.(e)
    # Although processes are spawned as in order of elements in collection,
    # the point when the message is sent to main process is pretty random

    Enum.map(pids, fn(pid) ->
      receive do 
        {^pid, result} -> IO.puts("result is #{result}")
      end
    end)
    # (Enum.map is blocking and sequential)
    # I think inclduing matching(^) in receive clause keeps unmatching messages
    # in the queue and then waits for the matching message with given pid
    # message lingering in the message queue will be tried when Enum.map moves on
    # It's mere my guess based on experiment.

  end
end

defmodule ParallelInsight do
  def map(collection, fun) do
    parent = self()

    # processes := pids
    pids = Enum.map(collection, fn(e) ->
      spawn_link(fn() -> 
        IO.puts("message #{e} received")
        send(parent, {self(), fun.(e)});
        IO.puts("message #{e} sent")
      end)
    end)

    Enum.map(pids, fn(pid) ->
      receive do 
        {^pid, result} -> IO.puts("result is #{result}")
        {pid, result} -> IO.puts("wrong !! #{result}")
      end
    end)

    # As mentioned above, 
  end
end

## main by jin

slow_double1 = fn(x) -> :timer.sleep(100*x); IO.puts(x * 2) end
slow_double2 = fn(x) -> :timer.sleep(100*x); x * 2 end

IO.puts("Enum.map start")
:timer.tc(fn() -> Enum.map([2,3,4,1], slow_double1) end) 

IO.puts("Parallel.map start")
:timer.tc(fn() -> Parallel.map([1,2,5,4,3], slow_double2) end)
# Parallel.map start
# message 1 received
# message 2 received
# message 5 received
# message 4 received
# message 3 received
# message 1 sent
# result is 2
# message 2 sent
# result is 4
# message 3 sent
# message 4 sent
# message 5 sent
# result is 10
# result is 8
# result is 6

IO.puts("ParallelInsight.map start")
:timer.tc(fn() -> ParallelInsight.map([1,2,4,5,3], slow_double2) end)
# ParallelInsight.map start
# message 1 received
# message 2 received
# message 4 received
# message 5 received
# message 3 received
# message 1 sent
# result is 2       # thank god it's 1
# message 2 sent
# result is 4       # thank god it's 2
# message 3 sent
# wrong !! 6        # because it's not 4
# message 4 sent
# wrong !! 8        # because it's not 5
# message 5 sent
# wrong !! 10       # because it's not 3
