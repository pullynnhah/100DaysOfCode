# Caesar Cipher

# Instructions

## Part 1: Encryption
Use [project01.py](project01.py) for this part.

#### TODO-1:
- Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
  
#### TODO-2:
- Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. e.g. 
```
plain_text = "hello"
shift = 5
cipher_text = "mjqqt"
print output: "The encoded text is mjqqt"
```

####HINT: How do you get the index of an item in a list:
[stackoverflow](https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list)

**Bug alert**: What happens if you try to encode the word `'civilization'`?
Since there are no characters after `z` in the alphabet list you get an `IndexError` if you try to access an index shift by any amount from it. 
- Just imagine that the list is circular (beginning -> end -> beginning). 
- To calculate the index you just have to do:
```python
index = index % len(list)
```
####TODO-3:
- Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# Example Output

```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello
Type the shift number:
> 19
The encoded text is: axeeh
```
OBS.: `>` represents input

## Part 2: Decryption
Use [project02.py](project02.py) for this part.

### TODO-1:
- Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  
### TODO-2:
- Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text. e.g.
```
cipher_text = "mjqqt"
shift = 5
plain_text = "hello"
print output: "The decoded text is hello"
```

### TODO-3:
- Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
- Then call the correct function based on that 'direction' variable. 
- You should be able to test the code to encrypt *AND* decrypt a message.

# Example Output

```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello
Type the shift number:
> 19
The encoded text is: axeeh
```
```
Type 'encode' to encrypt, type 'decode' to decrypt:
> decode
Type your message:
> axeeh
Type the shift number:
> 19
The decoded text is: hello
```
OBS.: `>` represents input

# Part 3: Reorganization
Use [project03.py](project03.py) for this part.

### TODO-1:
- Combine encrypt() and decrypt() functions into a single function called caesar().

### TODO-2:
- Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# Example Output

```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> paula
Type the shift number:
> 21061996
The encoded text is: vgarg
```
```
Type 'encode' to encrypt, type 'decode' to decrypt:
> decode
Type your message:
> vgarg
Type the shift number:
> 21061996
The decoded text is: paula
```
OBS.: `>` represents input

# Final Part: Final Touches
Use [project.py](project.py)

### TODO-1: 
- Import and print the logo from [caesar_cipher_art.py](caesar_cipher_art.py) when the program starts.

### TODO-2:
- What if the user enters a shift that is greater than the number of letters in the alphabet?
- Try running the program and entering a shift number of 45.
**Hint**: Think about how you can use the modulus (%).

### TODO-3:
- What happens if the user enters a number/symbol/space?
-Can you fix the code to keep the number/symbol/space when the text is encoded/decoded? e.g.
```
start_text = "meet me at 3"
end_text = "•••• •• •• 3"
```
### TODO-4:
- Can you figure out a way to ask the user if they want to restart the cipher program?
- e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
- If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
**Hint**: Try creating a new function that calls itself if they type 'yes'. 

# Example Output

```
           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd28"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> Paula is Gorgeous
Type the shift number:
> 21061996
The encoded text is: vgarg oy muxmkuay
Do you wish to continue? "yes" or "no":> yes
Type 'encode' to encrypt, type 'decode' to decrypt:
> decode
Type your message:
> vgarg oy muxmkuay
Type the shift number:
> 21061996
The decoded text is: paula is gorgeous
Do you wish to continue? "yes" or "no":> no
Goodbye!!!
```
OBS.: `>` represents input
