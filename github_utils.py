import os
from github import Github
import base64
import pandas as pd
from datetime import datetime

class GitHubManager:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.repo_name = os.getenv('GITHUB_REPO')  # format: "username/repository"
        self.github = Github(self.github_token)
        self.repo = self.github.get_repo(self.repo_name)
        
    def update_csv_file(self, name, email, student_id, grade):
        """Update the CSV file in GitHub repository with new submission."""
        file_path = 'data_submission.csv'
        new_data = {
            'Name': [name],
            'Email': [email],
            'Student_ID': [student_id],
            'Grade': [grade],
            'Submission_Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        }
        
        try:
            # Try to get existing file
            contents = self.repo.get_contents(file_path)
            existing_data = pd.read_csv(base64.b64decode(contents.content))
            
            # Append new data
            updated_data = pd.concat([
                existing_data,
                pd.DataFrame(new_data)
            ], ignore_index=True)
            
        except Exception as e:
            # File doesn't exist yet, create new DataFrame
            updated_data = pd.DataFrame(new_data)
        
        # Convert to CSV string
        csv_content = updated_data.to_csv(index=False)
        
        # Update or create file in repository
        try:
            contents = self.repo.get_contents(file_path)
            self.repo.update_file(
                file_path,
                f"Update submission data - {datetime.now()}",
                csv_content,
                contents.sha
            )
        except:
            # File doesn't exist, create it
            self.repo.create_file(
                file_path,
                f"Create submission data - {datetime.now()}",
                csv_content
            )
        
        return True
