# START:counter
defmodule Counter do
  use GenServer
# END:counter

  #####
  # External API
# START:counter
  def start_link do
    :gen_server.start_link(__MODULE__, nil, [])
  end
  def deliver_page(pid, ref, page) do
    :gen_server.cast(pid, {:deliver_page, ref, page})
  end
# END:counter

  #####
  # GenServer implementation
# START:counter

  def init(_args) do
    Parser.request_page(self()) # <label id="code.request_page_init"/>
    {:ok, nil}
  end

  def handle_cast({:deliver_page, ref, page}, state) do # <label id="code.deliver_page"/>
    Parser.request_page(self()) # <label id="code.request_page_deliver_page"/>

    words = String.split(page) # <label id="code.count_words_start"/>
    counts = Enum.reduce(words, HashDict.new, fn(word, counts) -> 
        Dict.update(counts, word, 1, &(&1 + 1))
      end) # <label id="code.count_words_end"/>
    Accumulator.deliver_counts(ref, counts) # <label id="code.deliver_counts_deliver_page"/>
    {:noreply, state}
  end
end
# END:counter

# START:supervisor
defmodule CounterSupervisor do
  use Supervisor.Behaviour
  def start_link(num_counters) do
    :supervisor.start_link(__MODULE__, num_counters) 
  end
  def init(num_counters) do
    workers = Enum.map(1..num_counters, fn(n) -> 
      worker(Counter, [], id: "counter#{n}")
    end)
    supervise(workers, strategy: :one_for_one)
  end
end
# END:supervisor
