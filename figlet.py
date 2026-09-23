import pyfiglet

print(pyfiglet.figlet_format(text="Figlet Preview",font="small"),end="")
print("")
print("         https://github.com/davidoberst",end="")
print("\n" + "-"*60 + "\n")

pyfiglet_fonts = [
    'alphabet', 'ascii9', 'ascii12', 'banner', 'big', 'bigascii9', 
    'bigascii12', 'bigmono9', 'bigmono12', 'block', 'bubble', 
    'circle', 'digital', 'emboss', 'emboss2', 'future', 'ivrit', 
    'lean', 'letter', 'mini', 'mnemonic', 'mono9', 'mono12', 
    'pagga', 'script', 'shadow', 'slant', 'small', 'smascii9', 
    'smascii12', 'smblock', 'smbraille', 'smmono9', 'smmono12', 
    'smscript', 'smshadow', 'smslant', 'standard', 'term', 'wideterm'
]
word = input("Text to preview : ")
for x in pyfiglet_fonts:
 try:
  print(f"---{x}")
  print(pyfiglet.figlet_format(text=word,font=x),end="")
  
 except:
  pass