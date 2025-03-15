### **🔗 Commands to Connect a Git Repository**  

#### **1️⃣ Clone an Existing Git Repository**
To download a repository from GitHub:
```sh
git clone https://github.com/your-username/repo-name.git  # Using HTTPS
# OR
git clone git@github.com:your-username/repo-name.git  # Using SSH
```
Move into the cloned repo:
```sh
cd repo-name
```

---

#### **2️⃣ Initialize a New Local Repository**
If you have an existing project and want to connect it to Git:
```sh
git init
```

---

#### **3️⃣ Add a Remote Repository**
Connect your local repo to GitHub:
```sh
git remote add origin https://github.com/your-username/repo-name.git  # Using HTTPS
# OR
git remote add origin git@github.com:your-username/repo-name.git  # Using SSH
```
Verify the connection:
```sh
git remote -v
```

---

#### **4️⃣ Add, Commit & Push Changes**
1. **Add all files to Git:**
   ```sh
   git add .
   ```
2. **Commit the changes:**
   ```sh
   git commit -m "Initial commit"
   ```
3. **Push to GitHub:**
   ```sh
   git branch -M main  # Rename to main if needed
   git push -u origin main
   ```

---
