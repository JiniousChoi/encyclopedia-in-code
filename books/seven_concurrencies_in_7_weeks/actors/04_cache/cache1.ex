defmodule Cache do
  # api
  def start_link do
    pid = spawn_link(__MODULE__, :loop, [HashDict.new, 0])
    Process.register(pid, :cache)
    pid
  end

  # api
  def put(url, page) do
    send(:cache, {:put, url, page})
  end

  # api
  def get(url) do
    ref = make_ref()
    send(:cache, {:get, self(), ref, url})
    receive do
      {:ok, ^ref, page} -> page
    end
  end

  # api
  def size do
    ref = make_ref()
    send(:cache, {:size, self(), ref})
    receive do
      {:ok, ^ref, s} -> s
    end
  end

  # api
  def terminate do
    send(:cache, {:terminate})
  end

  def loop(pages, size) do
    receive do
      {:put, url, page} ->
        new_pages = Dict.put(pages, url, page)
        new_size = size + byte_size(page) # <label id="code.bytesize"/>
        loop(new_pages, new_size)
      {:get, sender, ref, url} ->
        send(sender, {:ok, ref, pages[url]})
        loop(pages, size)
      {:size, sender, ref} ->
        send(sender, {:ok, ref, size})
        loop(pages, size)
      {:terminate} -> # Terminate request - don't recurse
    end
  end
end

defmodule CacheSupervisor do
  # api
  def start do
    spawn(__MODULE__, :loop_system, [])
  end

  def loop_system do
    Process.flag(:trap_exit, true)
    loop
  end

  def loop do
    pid = Cache.start_link
    receive do
      {:EXIT, ^pid, :normal} ->
        IO.puts("Cache exited normally")
        :ok
      {:EXIT, ^pid, reason} ->
        IO.puts("Cache failed with reason #{inspect reason} - restarting it")
        loop
    end
  end
end

Cache.start_link
# PID<0.47.0>

Cache.put("google.com", "Welcome to Google ...")
# {:put, "google.com", "Welcome to Google ..."}

IO.puts(Cache.get("google.com"))
# Welcome to Google ...

IO.puts(Cache.size())
# 21

# Exception handling is missing
# Cache.put("paulbutcher.com", nil)
# ** (EXIT from #PID<0.47.0>) an exception was raised:
#     ** (ArgumentError) argument error
#         :erlang.byte_size(nil)
#         cache1.ex:41: Cache.loop/2
