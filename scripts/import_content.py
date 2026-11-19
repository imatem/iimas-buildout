# Example script for uploading content

from Testing.makerequest import makerequest
from plone import api
from zope.component.hooks import setSite


import transaction


# 1. Initialize the Zope request and Plone site context
app = makerequest(app)
site = app["Plone"]  # Replace 'Plone' with your Plone site ID
setSite(site)

folder_type_name = 'ArticlesFolder'  # Portal type name of your custom Dexterity folder type
item_type_name = 'Article'  # Portal type name of your custom Dexterity type

ttool = api.portal.get_tool("portal_types")
fti = ttool.getTypeInfo(folder_type_name)
lang_title = api.portal.translate(fti.Title(), domain="imatem.cv", lang='es')
folder_title = lang_title.replace("Carpeta de ", "").capitalize()
lang_description = api.portal.translate(fti.Description(), domain="imatem.cv", lang='es')



userids = ['userid_1', 'userid_2'] # users with data to upload

# 2. Run all content operations inside the adopt_user context
with api.env.adopt_user(username="admin"):

    for userid in userids:
        # 3. Locate the target folder where items will be created
        # target_folder = site.restrictedTraverse("path/to/cvfolder")
        target_folder = site.restrictedTraverse(f"fsd/{userid}/cv")

        #3. Check if an object with this ID already exists in the target folder

        if target_folder.get(folder_type_name) == None:
            article_folder = api.content.create(
                container=target_folder,
                type=fti.getId(),
                title=folder_title,
                id=folder_type_name,
                description=lang_description,
            )
        custom_type_folder = target_folder.get(folder_type_name)

        # 4. Create the custom content item
        new_item = api.content.create(
            container=custom_type_folder,
            type=item_type_name,
            # replace with your article title
            title="My Article Item",
            # Custom schema fields passed as keyword arguments:
            article_status="published",
        )

        # 5. Commit the transaction to save changes to the ZODB
        transaction.commit()
        print(f"Successfully created {item_type_name}s in: {custom_type_folder.absolute_url()}")
