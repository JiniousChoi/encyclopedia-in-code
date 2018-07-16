defmodule Counter do
  def start(count) do
    spawn(__MODULE__, :loop, [count])
  end
  def next(counter) do
    send(counter, {:next})
  end
  def loop(count) do
    receive do
      {:next} ->
        IO.puts("Current count: #{count}")
        loop(count + 1)
    end
  end
end

# main logic by jin
counter = spawn(Counter, :loop, [1])
send(counter, {:next})
send(counter, {:next})
send(counter, {:next})

# give it some slack to consume all messages
import :timer, only: [ sleep: 1 ]
sleep(1000)
