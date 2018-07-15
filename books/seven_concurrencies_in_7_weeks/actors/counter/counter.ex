# START:loop
defmodule Counter do
# END:loop
# START_HIGHLIGHT
  def start(count) do
    spawn(__MODULE__, :loop, [count])
  end
# END_HIGHLIGHT
# START_HIGHLIGHT
  def next(counter) do
    send(counter, {:next})
  end
# END_HIGHLIGHT
# START:loop
  def loop(count) do
    receive do
      {:next} ->
        IO.puts("Current count: #{count}")
        loop(count + 1)
    end
  end
end
# END:loop
