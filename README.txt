Django tutorial from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website

Things I added:
    # Added a model.Language, with a row in the model.Books so it can populate model.Language simultaniously.
    # Used list_displays under admin.BookInstance to show more than just name.
    # Added inline listing of Book items to the Author detail view.
    # Added new block title on the index.html, seperate from base.html
    # Added Genre count on catalog page, index.html
    # Added Language to book_detail.html
    # Added author_detail.html and author_list.html
    # <strong>Had a lot of trouble with adding authenticated users with permissions.</strong> Mostly because I forgot to add it in admin screen. Created an template for librarians
        to see all books (not popualted with context yet), filled out the necessary pathways in urls.py. Completed and edited the original example view that would point to the
        new all_borrowd_books.html, updated models.py as needed, fixed my issue with the nav bar for users with permissions (I did not include the if user.is_staff block)
        and updated docs.

---
admin
111I111I1
---
testuser
testuserpassword123
---
librarian
librarianpassword123
---
Step-by-Step Setup Notes

Install venv (on local machine)
Engage venv (on local machine)
Install python
Install Django
Create workspace (on local machine)
Create project
Create app
Add app to settings.py
Add imports and paths to urlpatterns in url.py in main folder
Create url.py in app folder and add imports
Run server to see if it works - navigate to /admin/ to ensure it does
Add models
Add models you made into admin.py
Change the way the models are viewed in /admin/ by creating objects and registering them to the imported .models if need be
Create views in view.py of app
Create template folder in app - THIS IS WHERE YOUR HTML GOES
Create static folder in app - THIS IS WHERE LOCAL CSS GOES
Create base.html template
Extend to index.html and/or other apps if need be
Path urls properly in url.py(s)