# START:cache
defmodule Cache do
  # START_HIGHLIGHT
  use GenServer.Behaviour
  # END_HIGHLIGHT
# END:cache
  #####
  # External API

# START:api
  def start_link do
    :gen_server.start_link({:local, :cache}, __MODULE__, {HashDict.new, 0}, [])
  end

  def put(url, page) do
    :gen_server.cast(:cache, {:put, url, page})
  end

  def get(url) do
    :gen_server.call(:cache, {:get, url})
  end

  def size do
    :gen_server.call(:cache, {:size})
  end
# END:api

  #####
  # GenServer implementation

# START:cache
  def handle_cast({:put, url, page}, {pages, size}) do
    new_pages = Dict.put(pages, url, page)
    new_size = size + byte_size(page)
    {:noreply, {new_pages, new_size}}
  end
  def handle_call({:get, url}, _from, {pages, size}) do
    {:reply, pages[url], {pages, size}}
  end

  def handle_call({:size}, _from, {pages, size}) do
    {:reply, size, {pages, size}}
  end
end
# END:cache

# START:supervisor
defmodule CacheSupervisor do
# END:supervisor
  # START_HIGHLIGHT
  use Supervisor.Behaviour
  # END_HIGHLIGHT

# START:supervisorapi
  def start_link do
    :supervisor.start_link(__MODULE__, []) 
  end
# END:supervisorapi

# START:supervisor
  def init(_args) do
    workers = [worker(Cache, [])]
    supervise(workers, strategy: :one_for_one)
  end
end
# END:supervisor
