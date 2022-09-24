# Skills2022-Chireh
## Task 1
##### ● Task name => GitHub Skills Test 
##### ● Task preparation => Create a folder “Skills2022” in your DEVASC virtual machine and start a git repository.
##### ● Task implementation => To implement this task, first I create a folder “Skills2022” in your DEVASC virtual machine, after that I connected my local repository to an online repository on GitHub 
##### ● Task troubleshooting => in this task, have not encountered any problems.
##### ● Task verification =>  
###### Creation of a local repository in my VM  <br />
<img width="364" alt="task1 1-Create a local folder" src="https://user-images.githubusercontent.com/84504744/191972643-79b68910-12ef-40a7-a901-5eabb7da295f.png"> <br />
###### Connection between my local repository and Online Github repository  <br />
<img width="509" alt="task1 2-connected my local repository to online GIthub" src="https://user-images.githubusercontent.com/84504744/191979365-193349b6-c871-4a60-8a00-b763fca3abd8.png">


## Task 2
##### ● Task name => Ansible Skills Test
##### ● Task preparation => Write the Ansible script to install and test the websever with ping command in a single playbook.
##### ● Task implementation => To implement this task:<br />
Step 1: Enable the SSH server. <br />
Step 2: Edit the Ansible inventory file : in this step i was create 3 files, ansible.cfg, hosts and apache.yml. This is the content of these file: <br />
###### ansible.cfg 
<img width="213" alt="task2 5-content of the ansible cfg file" src="https://user-images.githubusercontent.com/84504744/192089259-e86aafdf-ef25-4185-89ad-209e180bf568.png"><br />
###### apache.yml 
<img width="299" alt="task2 6-content of the apache yml file" src="https://user-images.githubusercontent.com/84504744/192089273-38a2906d-7f6a-4aef-9388-f501d99b1cf0.png"><br />
###### hosts 
<img width="329" alt="task2 7-content of the hosts file" src="https://user-images.githubusercontent.com/84504744/192089277-780c74ac-1749-4a32-ab82-f32c2194baed.png"><br />
once these files were created, I run the Ansible playbook to install and test my apache2 webserver. 

##### ● Task troubleshooting => in this task, in the beginning I wanted to use my own virtual machine but I had problems with the virtual network card, in this case I decided to use the Labs virtual machine.
##### ● Task verification =>  
###### Playbook installing webserver apache2 and testing  <br />
<img width="953" alt="task2 2-PlayBook-installing-wabserver-apache2-and-testing" src="https://user-images.githubusercontent.com/84504744/192089578-b7f3b327-1dfa-444e-aefe-97c3f4fc84ae.png"><br />
###### verification the status of our apache2 server  <br />
<img width="523" alt="task2 3-verification-apache" src="https://user-images.githubusercontent.com/84504744/192089646-fe31ff52-65cc-4733-a54c-44a9ade60285.png"><br />
###### verification of our apache2 server in the Browser  <br />
<img width="953" alt="task2 4-verification-apache-browser" src="https://user-images.githubusercontent.com/84504744/192089682-0334d006-8881-4e91-8bfe-51fc251ea7b8.png"> <br />
###### Testing the server with a ping command <br />
<img width="401" alt="task2 8-testing-ping-command" src="https://user-images.githubusercontent.com/84504744/192089856-4e56832a-870a-470f-9ef4-ab3f948550c5.png"><br />
