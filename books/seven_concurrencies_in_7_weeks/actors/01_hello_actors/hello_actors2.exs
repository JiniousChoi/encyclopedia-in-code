defmodule Talker do
  def loop do
    receive do
      {:greet, name} -> IO.puts("Hello #{name}")
      {:praise, name} -> IO.puts("#{name}, you're amazing")
      {:celebrate, name, age} -> IO.puts("Here's to another #{age} years, #{name}")
      {:shutdown} -> exit(:normal)
    end
    loop
  end
end

Process.flag(:trap_exit, true)
# spawn and then link this main thread with the spawned actor thread
# `being linked` means, it will be explained later 
pid = spawn_link(&Talker.loop/0)
send(pid, {:greet, "Huey"})
send(pid, {:praise, "Dewey"})
send(pid, {:celebrate, "Louie", 16})
send(pid, {:shutdown})

receive do
  # this message is from the BEAM, since the :trap_exit is registered for the main thread.
  # ^(carot) is used for pattern matching, not for binding, to ensure that this message is
  # produced by the BEAM because of the spawned talker, not because of any other actors.
  {:EXIT, ^pid, reason} -> IO.puts("Talker has exited (#{reason})")
end
