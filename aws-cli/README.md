To create an **EC2 instance** using the **AWS CLI**, follow these steps:

---

### **Step 1: Configure AWS CLI (If Not Done Already)**
If you haven't set up AWS CLI, configure it using:
```sh
aws configure
```
It will prompt you for:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-east-1`)
- Default output format (e.g., `json`)

---

### **Step 2: Run the EC2 Instance Creation Command**
Use the following command to launch an EC2 instance:

```sh
aws ec2 run-instances \
    --image-id ami-xxxxxxxxxxxxxxxxx \
    --instance-type t2.micro \
    --key-name MyKeyPair \
    --security-group-ids sg-xxxxxxxx \
    --subnet-id subnet-xxxxxxxx \
    --count 1 \
    --associate-public-ip-address \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyEC2Instance}]'
```

---

### **Explanation of Parameters:**
- `--image-id ami-xxxxxxxxxxxxxxxxx` → Replace with the AMI ID of the OS you want (e.g., Amazon Linux, Ubuntu).
  - You can find AMI IDs using:
    ```sh
    aws ec2 describe-images --owners amazon --query 'Images[*].[ImageId,Name]' --output table
    ```
- `--instance-type t2.micro` → Defines the EC2 instance type (free-tier eligible).
- `--key-name MyKeyPair` → Replace with your SSH key pair name.
- `--security-group-ids sg-xxxxxxxx` → Replace with your security group ID.
- `--subnet-id subnet-xxxxxxxx` → Replace with the subnet ID in which to launch the instance.
- `--count 1` → Number of instances to launch.
- `--associate-public-ip-address` → Assigns a public IP address.
- `--tag-specifications` → Assigns a name tag to the instance.

---

### **Step 3: Verify the Instance**
After running the command, AWS CLI will return the instance details.  
To verify the instance:
```sh
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,PublicIpAddress]' --output table
```

This will show:
- **Instance ID**
- **Instance State (pending, running, etc.)**
- **Public IP Address** (if assigned)

---

### **Step 4: Connect to Your Instance (SSH)**
If the instance is running, connect to it using SSH:
```sh
ssh -i MyKeyPair.pem ec2-user@your-instance-ip
```


