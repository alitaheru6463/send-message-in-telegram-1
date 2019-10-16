import builtwith
wq='\t\t*******************************************************\n\n\n \t\t         telegram chanell : @persian_cyber_org \n\n\n\t\t*******************************************************'
print(wq)
id=input("\n\nid ? ? ?")
message=input("message ? ? ?")
pass1='9323'
q=4
w=0
n=input("what is password? ? ?")
if n == pass1:
    
    site = "http://persian-cyber.xyz/send-message/AR-MAN.php?message="+message+"&id="+id+"&pass=@Persian_Cyer_Org"
    mmd=builtwith.parse(site)
    print("ok")
else :
    print("error password")
    
input("T H E   E N D  .  .  .")
