defmodule Counter do
  def start(count) do
    spawn(__MODULE__, :loop, [count])
  end
  def next(counter) do
  # START_HIGHLIGHT
    ref = make_ref()
    send(counter, {:next, self(), ref})
    receive do
      {:ok, ^ref, count} -> count
    end
  # END_HIGHLIGHT
  end
  def loop(count) do
    receive do
      {:next, sender, ref} ->
        # START_HIGHLIGHT
        send(sender, {:ok, ref, count})
        # END_HIGHLIGHT
        loop(count + 1)
    end
  end
end
