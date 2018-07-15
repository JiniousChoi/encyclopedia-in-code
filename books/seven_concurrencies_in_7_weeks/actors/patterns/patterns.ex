# START:patterns
defmodule Patterns do
  def foo({x, y}) do
    IO.puts("Got a pair, first element #{x}, second #{y}")
  end
# END:patterns

# START:patterns2
  def foo({x, y, z}) do
    IO.puts("Got a triple: #{x}, #{y}, #{z}")
  end
# END:patterns2
# START:patterns
end
# END:patterns
