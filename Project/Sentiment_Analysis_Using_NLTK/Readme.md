# Sentiment Analysis Application

#### Problem Defination
Social media have received more attention nowadays. Twitter is one of the most popular social networking site where public and private opinion about a wide variety of subjects are expressed and spread continually. To analyse such a huge variety of data Sentiment Analysis application can be used. Sentiment Analysis can be used in several usecases. Analysising. Sentimet Analysis on any event.

#### Scope/Application
There are various application/scope of Sentiment Analysis. Below are some use case where Sentiment Analysis can be useful:
- It can be also use to identify potential threats emergin online regarding any religious event or topics.
- It can be helpful to take appropritate decision regarding any disaster  
- It can be used to give your business valuable insights into how people feel about your product brand or service and approprioate improvements can be done.
- It can be used to identify when potential negative threads are emerging online regarding your business, thereby allowing you to be proactive in dealing with it more quickly.
- In politics Sentiment Analysis can be used to keep track of political views, to detect consistency and inconsistency between statements and actions at the government level.
- Sentiment Analysis Dataset Twitter can be also used for analyzing election results.

#### Sentiment Analysis – Flow Diagram

Flow diagram is a collective term for a diagram representing a flow or set of dynamic relationships in a system. The term flow diagram is also used as a synonym for flowchart.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/flow_diagram.png" /></p>


------------
### Deploying project on AWS 

To deploy project on AWS, First creat an instance. Step to create instance are as given below:

- Click on “Services” at the upper left corner on AWS main console and you will see the following screen with all the services available on AWS. Click on "EC2" available under “Compute.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Main_console.PNG" /></p>

- To create an instance, click on "Launch Instance"

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Launch_Instance.PNG" /></p>

- You can select an AMI of your choice. Here, we will proceed with "Ubuntu Server 18.04". If you are using a Free Tier Account, make sure to select the AMI which is eligible for Free Tier Usage else you will be charged for it. "Ubuntu Server 18.04" is eligible for Free Tier so you can proceed with this.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/choose_ami.PNG" /></p>

- Once you have selected an AMI, it's time to select the Instance Type. Here, we shall proceed with "t2.micro" as it is eligible for Free Tier Account.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Choose_Instance_Type.PNG" /></p>

- On this screen, you can specify the details or you can just click on "Next: Add Storage" to proceed with the default settings. Here, we shall proceed with the default settings.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/configure_instance.PNG" /></p>

- You can specify the size for the root partition. I have just proceed with the default Root Partition Size as 8 GBs. Click on “Next: Add Tags” to proceed.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Add_Storage.PNG" /></p>

- You can specify Tags (Key:Value) or can skip this step and click on “Next: Configure Security Group”

- If you have an existing Security Group you can select that or can create a new. We shall create a new Security Group by just selecting “Create a new Security Group” radio button. Click on "Review and Launch"

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/comfigre_security_group.PNG" /></p>

- Now, review your configuration and click on “Launch”

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/review_and_launch.PNG" /></p>

- Before the instance creation starts, we need to select a Key-Pair which is then required to take ssh access to the server. To create a new Key-Pair, select “Create a new Key-Pair” from the drop-down menu, give a name to the Key-Pair and download it. Keep this Key-Pair at a safe place.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/key%20pair.PNG" /></p>

- Wait for some time until the instance gets created. Click on “View Instances” to check the Instance State and other details.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/instance_created.PNG" /></p>

- Once the Instance State changes from “pending” to ‘running’ you can connect to the instance.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/All_Instances.PNG" /></p>

Once the instance is created, Connect to the Linux/Ubuntu instances that you launched and transfer files between your local computer and your instance.

#### Connection options
The operating system of your local computer determines the options that you have to connect from your local computer to your Linux instance.

- If your local computer operating system is Linux or macOS X
	- SSH client
	- EC2 Instance Connect
	- AWS Systems Manager Session Manager
- If your local computer operating system is Windows
	- PuTTY
	- SSH client
	- AWS Systems Manager Session Manager
	- Windows Subsystem for Linux

#### Connecting to your Linux instance from Windows using PuTTY

##### Convert your private key using PuTTYgen
PuTTY does not natively support the private key format for SSH keys. PuTTY provides a tool named PuTTYgen, which converts keys to the required format for PuTTY. You must convert your private key (.pem file) into this format (.ppk file) as follows in order to connect to your instance using PuTTY.

*To convert your private key*
1. From the Start menu, choose All Programs, PuTTY, PuTTYgen.

2. Under Type of key to generate, choose RSA. If you're using an older version of PuTTYgen, choose SSH-2 RSA.
![type of key to generate](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/puttygen-key-type.png)

3. Choose Load. By default, PuTTYgen displays only files with the extension .ppk. To locate your .pem file, choose the option to display files of all types.
![locate pem file](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/puttygen-load-key.png)

4. Select your .pem file for the key pair that you specified when you launched your instance and choose Open. PuTTYgen displays a notice that the .pem file was successfully imported. Choose OK.

5. To save the key in the format that PuTTY can use, choose Save private key. PuTTYgen displays a warning about saving the key without a passphrase. Choose Yes.
6. Specify the same name for the key that you used for the key pair (for example, my-key-pair) and choose Save. PuTTY automatically adds the .ppk file extension.

Your private key is now in the correct format for use with PuTTY. You can now connect to your instance using PuTTY's SSH client.

##### To connect to your instance using PuTTY

1. Start PuTTY (from the Start menu, choose All Programs, PuTTY, PuTTY).

2. In the Category pane, choose Session and complete the following fields:

- a. In the Host Name box, do one of the following:
	- (Public DNS) To connect using your instance's public DNS name, enter my-instance-user-name@my-instance-public-dns-name.
	- (IPv6) Alternatively, if your instance has an IPv6 address, to connect using your instance's IPv6 address, enter my-instance-user-name@my-instance-IPv6-address.

For information about how to get the user name for your instance, and the public DNS name or IPv6 address of your instance, see Get information about your instance.

- b. Ensure that the Port value is 22.

- c. Under Connection type, select SSH.

![Putty Session Configuration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/putty-session-config.png)

3. (Optional) You can configure PuTTY to automatically send 'keepalive' data at regular intervals to keep the session active. This is useful to avoid disconnecting from your instance due to session inactivity. In the Category pane, choose Connection, and then enter the required interval in the Seconds between keepalives field. For example, if your session disconnects after 10 minutes of inactivity, enter 180 to configure PuTTY to send keepalive data every 3 minutes.

4. In the Category pane, expand Connection, expand SSH, and then choose Auth. Complete the following:
	a. Choose Browse.
	b. Select the .ppk file that you generated for your key pair and choose Open.
	c. (Optional) If you plan to start this session again later, you can save the session information for future use. Under Category, choose Session, enter a name for the session in Saved Sessions, and then choose Save.
	d. Choose Open.
5. If this is the first time you have connected to this instance, PuTTY displays a security alert dialog box that asks whether you trust the host to which you are connecting.
	a. (Optional) Verify that the fingerprint in the security alert dialog box matches the fingerprint that you previously obtained in (Optional) Get the instance fingerprint. If these fingerprints don't match, someone might be attempting a "man-in-the-middle" attack. If they match, continue to the next step.
	b. Choose Yes. A window opens and you are connected to your instance.

##### Transferring files to your Linux instance using WinSCP

To use WinSCP, you need the private key that you generated in Convert your private key using PuTTYgen. You also need the public DNS name of your Linux instance.

1. Start WinSCP.

2. At the WinSCP login screen, for Host name, enter one of the following:
	- (Public DNS or IPv4 address) To log in using your instance's public DNS name or public IPv4 address, enter the public DNS name or public IPv4 address for your instance.
	- (IPv6) Alternatively, if your instance has an IPv6 address, to log in using your instance's IPv6 address, enter the IPv6 address for your instance.

3. For User name, enter the default user name for your AMI.
	- For Amazon Linux 2 or the Amazon Linux AMI, the user name is ec2-user.
	- For a CentOS AMI, the user name is centos.
	- For a Debian AMI, the user name is admin or root.
	- For a Fedora AMI, the user name is ec2-user or fedora.
	- For a RHEL AMI, the user name is ec2-user or root.
	- For a SUSE AMI, the user name is ec2-user or root.
	- For an Ubuntu AMI, the user name is ubuntu.
	- Otherwise, if ec2-user and root don't work, check with the AMI provider.

4. Specify the private key for your instance. For Private key, enter the path to your private key, or choose the "..." button to browse for the file. To open the advanced site settings, for newer versions of WinSCP, choose Advanced. To find the Private key file setting, under SSH, choose Authentication. Here is a screenshot from WinSCP version 5.9.4: WinSCP requires a PuTTY private key file (.ppk). You can convert a .pem security key file to the .ppk format using PuTTYgen. For more information, see Convert your private key using PuTTYgen.
![WinSCP Key Pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/WinSCP-keypair.png)

5. (Optional) In the left panel, choose Directories. For Remote directory, enter the path for the directory to which to add files. To open the advanced site settings for newer versions of WinSCP, choose Advanced. To find the Remote directory setting, under Environment, choose Directories.

6. Choose Login. To add the host fingerprint to the host cache, choose Yes.
![WinSCP Connection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/WinSCP-connection.png)

7. After the connection is established, in the connection window your Linux instance is on the right and your local machine is on the left. You can drag and drop files directly into the remote file system from your local machine

After uploading all the files, open the terminal from putty and execute your project. Using the DNS of instance you can run program from anywhere in any web browser.