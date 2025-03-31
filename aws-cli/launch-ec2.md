Here’s a **step-by-step guide** to create an **EC2 instance via AWS CLI**, including generating a **new key pair** and **security group**.

---

## **Step 1: Configure AWS CLI (If Not Done Yet)**
If you haven’t set up AWS CLI, run:
```bash
aws configure
```
Enter:
- **Access Key ID**
- **Secret Access Key**
- **Region (e.g., us-east-1)**
- **Output format (json/text/table)**

---

## **Step 2: Create a Key Pair**
A key pair is required to SSH into your EC2 instance.

```bash
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem
```
✅ **Secure the key file**:
```bash
chmod 400 MyKeyPair.pem
```
> **Note:** Replace `MyKeyPair` with your preferred key name.

---

## **Step 3: Create a Security Group**
A security group defines firewall rules for your instance.

```bash
aws ec2 create-security-group --group-name MySecurityGroup --description "My custom security group"
```
This will return a **Group ID** (e.g., `sg-0123456789abcdef0`). Copy it for later use.

✅ **Allow SSH (Port 22) and HTTP (Port 80) access**:
```bash
aws ec2 authorize-security-group-ingress --group-id sg-0123456789abcdef0 --protocol tcp --port 22 --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress --group-id sg-0123456789abcdef0 --protocol tcp --port 80 --cidr 0.0.0.0/0
```

> **Security Tip**: Instead of `0.0.0.0/0`, use your specific IP (`your_ip/32`) for SSH.

---

## **Step 4: Find an AMI ID**
Find an **Amazon Linux 2 AMI ID**:
```bash
aws ec2 describe-images --owners amazon --filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" --query 'Images[0].[ImageId]' --output text
```
Copy the **AMI ID** (e.g., `ami-0abcdef1234567890`).

---

## **Step 5: Find a Subnet ID**
List available subnets:
```bash
aws ec2 describe-subnets --query 'Subnets[*].[SubnetId,AvailabilityZone]' --output table
```
Pick a **Subnet ID** (e.g., `subnet-0123456789abcdef0`).

---

## **Step 6: Launch an EC2 Instance**
Now, create the EC2 instance using the key pair, security group, and subnet.

```bash
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --count 1 \
    --instance-type t2.micro \
    --key-name MyKeyPair \
    --security-group-ids sg-0123456789abcdef0 \
    --subnet-id subnet-0123456789abcdef0 \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyFirstInstance}]'
```
✅ **What this does:**
- Uses the **AMI ID** for Amazon Linux 2.
- Launches **one instance** (`--count 1`).
- Uses **t2.micro** instance type (**Free Tier Eligible**).
- Associates the **key pair** `MyKeyPair.pem` (for SSH access).
- Uses the **security group** (`sg-0123456789abcdef0`).
- Assigns a **tag** ("MyFirstInstance").

---

## **Step 7: Get the Public IP**
To check if the instance is running and retrieve its public IP:
```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,PublicIpAddress]' --output table
```
---

## **Step 8: Connect to Your Instance**
Once your instance is running, connect via SSH:
```bash
ssh -i MyKeyPair.pem ec2-user@<Public-IP>
```
Replace `<Public-IP>` with the instance's actual **public IP address**.

---

### **🎯 Done! Your EC2 Instance Is Now Running.**

