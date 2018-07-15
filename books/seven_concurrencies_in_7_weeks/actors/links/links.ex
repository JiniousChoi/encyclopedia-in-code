# START:loop
defmodule LinkTest do
  def loop do
    receive do
      {:exit_because, reason} -> exit(reason)
      {:link_to, pid} -> Process.link(pid)
      {:EXIT, pid, reason} -> IO.puts("#{inspect(pid)} exited because #{reason}")
    end
    loop
  end
# END:loop

# START:loop_system
  def loop_system do
    Process.flag(:trap_exit, true)
    loop
  end
# END:loop_system
# START:loop
end
# END:loop
