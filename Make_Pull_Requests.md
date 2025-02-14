# **How to contribute to a collaborative repository: Basic steps**  

In this scenario, we will learn how to fork a repository associated with a collaborative project, create a new branch, add a file, push your changes, and make a pull request. You will also see how to handle conflicts if they arise during the process.  


## **Step 1: Fork the Main Repository**  
Forking creates a personal copy of the main repository in your GitHub account. This allows you to make changes without affecting the original repository.  

1. Go to the main repository:  
   [https://github.com/omidvarnia/git_tutorial](https://github.com/omidvarnia/git_tutorial)  
2. Click the **Fork** button (top right).  
3. This creates a copy of the repository in your own GitHub account (**my_username/git_tutorial**).

Replace `my_username` with your GitHub username.  


## **Step 2: Clone Your Forked Repository**  
Cloning downloads your forked repository to your local computer so you can work on it.  

1. Open your terminal.  
2. Run the following command to clone your forked repository:  

   ```sh
   git clone https://github.com/my_username/git_tutorial.git
   cd git_tutorial

## **Step 3: Create a New Branch**  
A branch allows you to work on changes separately from the main code. This keeps your changes organized and prevents conflicts.  

1. Run:  

   ```sh
   git checkout -b test_branch

You can choose any name for your ney branch (here, I have chosen `test_branch` as an example).

## **Step 4: Add a New File**  
You will now create a new file to simulate making a change in the repository.  

1. Create a new text file, e.g., `myfile.txt`.  
2. Add some text inside it (e.g., `"This is my first contribution"`).  
3. Save the file.  

## **Step 5: Commit and Push the Changes**  
Committing saves your changes locally, and pushing uploads them to GitHub.  

1. Add the file:  

   ```sh
   git add myfile.txt
   ```

2. Commit the changes:  

   ```sh
   git commit -m "Added myfile.txt"
   ```

3. Push the changes to your new branch:  

   ```sh
   git push origin test_branch
   ```
## **Step 6: Create a Pull Request (PR)**  
A pull request lets the owner of the original repository review and merge your changes.  

1. Go to your forked repository on GitHub:  
   [https://github.com/my_username/git_tutorial](https://github.com/my_username/git_tutorial)  
2. Click **Compare & pull request**.  
3. Choose the main repository’s branch (`main`) as the target.  
4. Click **Create pull request**.  

## **Step 7: Handle Conflicts (If Any)**  
Conflicts happen when two people change the same part of a file. You need to fix them before your changes can be merged.  

1. If there is a conflict, GitHub will show a message.  
2. Click **Resolve conflicts** and follow the instructions.  
3. After resolving, click **Commit merge**.  
4. Click **Re-request review** if needed.  

## **Step 8: Merge the Pull Request**  
Once your pull request is approved, you can merge your changes into the main repository.  

1. Wait for approval from the repository owner.  
2. Once approved, click **Merge pull request**.  

Now, your changes are in the main repository.
