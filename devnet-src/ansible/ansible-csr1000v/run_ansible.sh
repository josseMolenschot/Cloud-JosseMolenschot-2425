ansible-playbook -i hosts.yml checklocalinfo.yml > localinfo.txt
cat localinfo.txt | grep -m 1 "Cisco IOS"

#> localinfo.txt