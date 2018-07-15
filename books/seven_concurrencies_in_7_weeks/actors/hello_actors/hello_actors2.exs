# START:talker
defmodule Talker do
  def loop do
    receive do
      {:greet, name} -> IO.puts("Hello #{name}")
      {:praise, name} -> IO.puts("#{name}, you're amazing")
      {:celebrate, name, age} -> IO.puts("Here's to another #{age} years, #{name}")
      # START_HIGHLIGHT
      {:shutdown} -> exit(:normal)
      # END_HIGHLIGHT
    end
    loop
  end
end
# END:talker

# START:spawn
Process.flag(:trap_exit, true)
pid = spawn_link(&Talker.loop/0)
# END:spawn

# START:main
send(pid, {:greet, "Huey"})
send(pid, {:praise, "Dewey"})
send(pid, {:celebrate, "Louie", 16})
# START_HIGHLIGHT
send(pid, {:shutdown})
# END_HIGHLIGHT

# START_HIGHLIGHT
receive do
  {:EXIT, ^pid, reason} -> IO.puts("Talker has exited (#{reason})")
end
# END_HIGHLIGHT
# END:main