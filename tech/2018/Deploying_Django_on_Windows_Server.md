# Deploying Django on Windows Server

## 2018/1/4

## IIS8.5 on Windows Server 2012
This is a successful attempt to deploy django app on IIS.

## Step

* install wsgi, python package developed by microsoft teams
* run `wsgi-enable`
* create a new file called `web.config` in the root directory of website

```XML
<configuration>
  <system.webServer>
    <handlers>
            <remove name="StaticFile" />
      <add name="Python FastCGI" path="*" verb="*" modules="FastCgiModule" scriptProcessor="path_to_your_python_directory\python.exe|path_to_the_wfastcgi_python_directory\wfastcgi.py" resourceType="Unspecified" requireAccess="Script" />
    </handlers>
  </system.webServer>

  <appSettings>
    <!-- Required settings -->
    <add key="WSGI_HANDLER" value="django.core.wsgi.get_wsgi_application()" />
    <add key="PYTHONPATH" value="path_to_the_root_directory_of_website" />

    <!-- Optional settings -->
    <add key="WSGI_LOG" value="path_to_the_log_directory" />
    <add key="DJANGO_SETTINGS_MODULE" value="mysite.settings" />    
  </appSettings>
</configuration>
```

* create a website in IIS Manager
* unlock the `handler` if necessary, by default `handler` rewritting is invalid. We can unlock it by modifying
`applicationHost.config` in `%windir%\system32\inetsrv\config\` with Notepad.   
* django app `setting.debug=False`
* add a virtual directory in IIS, pointing to the static root directory of django app
* allow anonymous visit with app pool authentication, not IIS_USER authentication if necessary


## Issue remained
During this attempt, I found that
filenames can not have german characters when I run django collectstatic command.
