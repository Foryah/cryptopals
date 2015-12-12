defmodule Set1 do                                                             
  def hex_to_str(hex_input) do
    hex_input
    |> Base.decode16!(case: :lower) 
  end

  def hex_to_b64(hex_input) do
    hex_input
    |> hex_to_str
    |> Base.encode64()
  end
end


# TODO: Find a way to put the tests in another file
ExUnit.start                                                                                              
                                                                                 
defmodule TestSet1 do                                                             
  use ExUnit.Case                                                                

  test "Hex to String" do
    assert Set1.hex_to_str("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "I'm killing your brain like a poisonous mushroom"
  end

  test "Hex to Base64" do
    assert Set1.hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
  end
end
