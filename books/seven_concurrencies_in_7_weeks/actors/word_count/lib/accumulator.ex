# START:accumulator
defmodule Accumulator do
  use GenServer
# END:accumulator

  #####
  # External API
# START:accumulator

  def start_link do
    :gen_server.start_link({:global, :wc_accumulator}, __MODULE__, # <label id="code.accumulator_start_link"/>
      {HashDict.new, HashSet.new}, [])
  end

  def deliver_counts(ref, counts) do
    :gen_server.cast({:global, :wc_accumulator}, {:deliver_counts, ref, counts}) # <label id="code.accumulator_deliver_counts"/>
  end
# END:accumulator

  def get_results do
    :gen_server.call({:global, :wc_accumulator}, {:get_results})
  end

  #####
  # GenServer implementation
# START:accumulator

  def handle_cast({:deliver_counts, ref, counts}, {totals, processed_pages}) do
    if Set.member?(processed_pages, ref) do
      {:noreply, {totals, processed_pages}}
    else
      new_totals = Dict.merge(totals, counts, fn(_k, v1, v2) -> v1 + v2 end)
      new_processed_pages = Set.put(processed_pages, ref)
      Parser.processed(ref)
      {:noreply, {new_totals, new_processed_pages}}
    end
  end
# END:accumulator

  def handle_call({:get_results}, _, {totals, processed_pages}) do
    {:reply, {totals, processed_pages}, {totals, processed_pages}}
  end
# START:accumulator
end
# END:accumulator

defmodule AccumulatorSupervisor do
  use Supervisor.Behaviour

  def start_link do
    :supervisor.start_link(__MODULE__, []) 
  end

  def init(_args) do
    workers = [worker(Accumulator, [])]
    supervise(workers, strategy: :one_for_one)
  end
end
