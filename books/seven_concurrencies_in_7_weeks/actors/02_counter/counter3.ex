defmodule Counter do
  def loop(count) do
    receive do
      {:next, sender, ref} ->
        send(sender, {:ok, ref, count})
        loop(count + 1)
    end
  end

  # API
  def start(count) do
    pid = spawn(__MODULE__, :loop, [count])
    Process.register(pid, :counter) # HIGHLIGHT
    pid
  end

  # API
  def next do
    ref = make_ref()
    send(:counter, {:next, self(), ref}) # HIGHLIGHT
    receive do
      {:ok, ^ref, count} -> IO.puts(count)
    end
  end
end

# main by jin
pid = Counter.start(33)
Counter.next()
Counter.next()
Counter.next()

