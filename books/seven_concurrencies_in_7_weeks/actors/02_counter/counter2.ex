defmodule Counter do
  def start(count) do
    spawn(__MODULE__, :loop, [count])
  end
  def next(counter) do
    ref = make_ref()
    send(counter, {:next, self(), ref})
    receive do
      {:ok, ^ref, count} -> count # IO.puts(count)
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

# main by jin
pid = Counter.start(42)
Process.register(pid, :counter)
counter = Process.whereis(:counter)
Counter.next(counter)
# Counter.next(counter)
send(:counter, {:next, self(), make_ref()})
receive do msg -> msg end

# ===== Simulation on elixir repl =====
# iex(1)> pid = Counter.start(42)
# #PID<0.63.0>
# iex(2)> Process.register(pid, :counter)
# true
# iex(3)> Process.whereis(:counter)
# #PID<0.63.0>
# iex(4)> Counter.next(counter)
# 42
# iex(5)> Counter.next(counter)
# 43
# iex(6)> Process.registered
# [IEx.Config, :standard_error_sup, IEx.Supervisor, Logger, :erl_prim_loader,
#  :rex, :kernel_sup, :inet_db, :global_name_server, Logger.Supervisor,
#  :code_server, :error_logger, :init, :elixir_counter, :counter, :file_server_2,
#  :user, :elixir_config, :elixir_sup, :application_controller,
#  :elixir_code_server, Logger.Watcher, :user_drv, :standard_error,
#  :kernel_safe_sup, :global_group]

