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

#### Deploying project on AWS 
- Click on “Services” at the upper left corner on AWS main console and you will see the following screen with all the services available on AWS. Click on "EC2" available under “Compute.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Main_console.PNG" /></p>

- To create an instance, click on "Launch Instance"

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Launch_Instance.PNG" /></p>

You can select an AMI of your choice. Here, we will proceed with "Ubuntu Server 18.04". If you are using a Free Tier Account, make sure to select the AMI which is eligible for Free Tier Usage else you will be charged for it. "Ubuntu Server 18.04" is eligible for Free Tier so you can proceed with this.


<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/choose_ami.PNG" /></p>

Once you have selected an AMI, it's time to select the Instance Type. Here, we shall proceed with "t2.micro" as it is eligible for Free Tier Account.


<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Choose_Instance_Type.PNG" /></p>

On this screen, you can specify the details or you can just click on "Next: Add Storage" to proceed with the default settings. Here, we shall proceed with the default settings.


<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/configure_instance.PNG" /></p>

You can specify the size for the root partition. I have just proceed with the default Root Partition Size as 8 GBs. Click on “Next: Add Tags” to proceed.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/Add_Storage.PNG" /></p>

You can specify Tags (Key:Value) or can skip this step and click on “Next: Configure Security Group”

If you have an existing Security Group you can select that or can create a new. We shall create a new Security Group by just selecting “Create a new Security Group” radio button. Click on "Review and Launch"


<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/comfigre_security_group.PNG" /></p>

Now, review your configuration and click on “Launch”

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/review_and_launch.PNG" /></p>

Before the instance creation starts, we need to select a Key-Pair which is then required to take ssh access to the server. To create a new Key-Pair, select “Create a new Key-Pair” from the drop-down menu, give a name to the Key-Pair and download it. Keep this Key-Pair at a safe place.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/key%20pair.PNG" /></p>

Wait for some time until the instance gets created. Click on “View Instances” to check the Instance State and other details.


<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/instance_created.PNG" /></p>

Once the Instance State changes from “pending” to ‘running’ you can connect to the instance.

<p align="center"><img src="https://github.com/isaacramthal/deepak.bhavsar-works/blob/feature/Sentiment_Analysis_NLTK/Project/Sentiment_Analysis_Using_NLTK/snapshots/All_Instances.PNG" /></p>








