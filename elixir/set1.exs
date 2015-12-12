defmodule Set1 do                                                             
  use Bitwise

  def hex_to_str(hex_input) do
    hex_input
    |> Base.decode16!(case: :lower) 
  end

  def str_to_hex(str_input) do
    str_input
    |> Base.encode16(case: :lower)
  end

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
end
