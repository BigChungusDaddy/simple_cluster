defmodule SimpleCluster.Executer do
  use GenServer
  require Logger

  def start_link(_), do: GenServer.start_link(__MODULE__, %{})

  @impl GenServer
  def init(state) do
    :net_kernel.monitor_nodes(true)
    {:ok, state}
  end

  @impl GenServer
  def handle_info(term, state) do
    {:noreply, state}
  end

  def send_command(function_name) do
    # Run async and give a timeout
    task = Task.async(fn ->
      Rambo.run(function_name)
    end)
    {:ok, result} = Task.await(task)
    output = String.split(result.out, "\n")
    Enum.each(output, fn x -> IO.puts x end)
  end

  def send_command(function_name, args_or_options) do
    task = Task.async(fn ->
      Rambo.run(function_name, args_or_options)
    end)
    {:ok, result} = Task.await(task)
    output = String.split(result.out, "\n")
    Enum.each(output, fn x -> IO.puts x end)
  end

  def send_command(function_name, args, opts) do
    task = Task.async(fn ->
      Rambo.run(function_name, args, opts)
    end)
    {:ok, result} = Task.await(task)
    output = String.split(result.out, "\n")
    Enum.each(output, fn x -> IO.puts x end)
  end

end
