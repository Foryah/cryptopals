defmodule Set1 do                                                             
  use Bitwise

  def hex_to_str(hex_input), do: Base.decode16!(hex_input, case: :lower) 
  def str_to_hex(str_input), do: Base.encode16(str_input, case: :lower)

  def hex_to_b64(hex_input) do
    hex_input
    |> hex_to_str
    |> Base.encode64()
  end

  # Doing my best not to write 'smart code' but clear code...
  def hex_xor(hex_input1, hex_input2) do
    input1 = hex_to_str(hex_input1)
    input2 = hex_to_str(hex_input2)

    input1_char_list = to_char_list(input1)
    input2_char_list = to_char_list(input2)

    result_char_list = xor_lists(input1_char_list, input2_char_list)

    result = to_string(result_char_list) 
    str_to_hex(result)
  end

  defp xor_lists([h1], [h2]), do: h1 ^^^ h2
  defp xor_lists([h1|t1], [h2|t2]), do: [h1 ^^^ h2, xor_lists(t1, t2)]

  def single_byte_xor(hex_string) do
    hex_string
    |> decrypt_with_keys_in_range(0..255)
    |> append_scores_to_results() 
    |> select_best_result([])
  end

  defp append_scores_to_results(result_list) do
    result_list
    |> Enum.map(fn(line) -> append_score_to_one_line(line) end)
  end

  defp append_score_to_one_line(line) do
    [_, {_, result}] = line
    line ++ [score: score_for_line(result)]
  end

  defp score_for_line(line) do
    char_list = to_char_list(line)
    do_score_for_line(char_list)
  end

  defp do_score_for_line([]), do: 0
  defp do_score_for_line([head|tail]), do: score_for_letter([head]) + do_score_for_line(tail)

  defp score_for_letter(letter) do
    s_letter = String.downcase(to_string(letter))
    case s_letter do
      "e" -> 13
      "t" -> 9
      "a" -> 8
      "o" -> 8
      "n" -> 7
      "i" -> 7
      "r" -> 7
      "s" -> 6
      "h" -> 6
      "l" -> 4
      "d" -> 4
      "c" -> 3
      "u" -> 3
      "p" -> 3
      "f" -> 3
      "m" -> 2
      "w" -> 2
      "y" -> 2
      "b" -> 1
      "g" -> 1
      "v" -> 1
      " " -> 4
      _ -> 0
    end
  end

  defp select_best_result([], best), do: best
  defp select_best_result([head|tail], best) when best == [], do: select_best_result(tail, head)
  defp select_best_result([head|tail], best) do
    [_, _, {_, score}] = head
    [_, _, {_, best_score}] = best
    if best_score > score do
      select_best_result(tail, best)
    else
      select_best_result(tail, head)
    end
  end

  defp decrypt_with_keys_in_range(input, range) do
    Enum.map(range, fn(key) -> [key: key, result: byte_xor_line(input, <<key :: size(8)>>)] end)
  end

  defp byte_xor_line(line, byte) do 
    Enum.map(1..trunc(String.length(line)/2), fn(_) -> byte end)
    |> to_string 
    |> str_to_hex
    |> hex_xor(line)
    |> hex_to_str
  end

  def file_single_byte_xor(path_to_file) do
    path_to_file
    |> File.read!
    |> String.split("\n")
    |> Enum.map(&single_byte_xor(&1))
    |> select_best_result([])
  end
end


# TODO: Find a way to put the tests in another file
ExUnit.start                                                                                              
                                                                                 
defmodule TestSet1 do                                                             
  use ExUnit.Case                                                                

  test "Hex to String" do
    assert Set1.hex_to_str("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "I'm killing your brain like a poisonous mushroom"
  end

  test "String to Hex" do
    assert Set1.str_to_hex("I'm killing your brain like a poisonous mushroom") == "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
  end

  test "Hex to Base64" do
    assert Set1.hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
  end

  test "Hex XOR Hex" do
    assert Set1.hex_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"
  end

  test "Single byte xor" do
    [_, {_, result}, _] = Set1.single_byte_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    assert result == "Cooking MC's like a pound of bacon"
  end

  test "File Single byte xor" do
    Set1.file_single_byte_xor("../data/xored_data")
  end
end
