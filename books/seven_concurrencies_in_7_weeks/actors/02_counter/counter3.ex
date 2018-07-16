defmodule Counter do
  def loop(count) do
    receive do
      {:next, sender, ref} ->
        send(sender, {:ok, ref, count})
        loop(count + 1)
    end
  end

# START:api
  def start(count) do
    pid = spawn(__MODULE__, :loop, [count])
    # START_HIGHLIGHT
    Process.register(pid, :counter)
    # END_HIGHLIGHT
    pid
  end
  def next do
    ref = make_ref()
    # START_HIGHLIGHT
    send(:counter, {:next, self(), ref})
    # END_HIGHLIGHT
    receive do
      {:ok, ^ref, count} -> count
    end
  end
# END:api
end
