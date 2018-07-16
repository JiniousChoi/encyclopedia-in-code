defmodule Counter do
  def start(count) do
    spawn(__MODULE__, :loop, [count])
  end
  def next(counter) do
    ref = make_ref()
    send(counter, {:next, self(), ref})
    receive do
      {:ok, ^ref, count} -> count
    end
  end
  def loop(count) do
    receive do
      {:next, sender, ref} ->
        send(sender, {:ok, ref, count})
        loop(count + 1)
    end
  end
end

# iex(1)> counter = Counter.start(42)
# #PID<0.63.0>
# iex(2)> Counter.next(counter)
# 42
# iex(3)> Counter.next(counter)
# 43

