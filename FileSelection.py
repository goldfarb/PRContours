# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load toolboxes
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Conversion Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


#  variables
#States = "States"
#States2 = "States"
pytry = "C:\\CSPT Studies\\pytry"
pytry2 = "C:\\CSPT Studies\\pytry"

StateAb = ['AL','AZ','NY']

for StateA in StateAb:
	
	# Process: Select Layer By Attribute...
	#i ='"States", "NEW_SELECTION", "STATE_ABBR" = %r' % StateA
	gp.SelectLayerByAttribute_management("States", "NEW_SELECTION", "STATE_ABBR = 'AL'")

	# Process: Feature Class To Shapefile (multiple)...
	gp.FeatureClassToShapefile_conversion("States", pytry__2_)

	os.rename ("C:\CSPT Studies\pytry\States.dbf","C:\CSPT Studies\pytry\States\%m.xls") % StateA

	#ending = ['shx','shp.xml','shp','sbx','sbn','prj']

	#for end in ending:
    #	x = "C:\CSPT Studies\pytry\States.%s" % end
    #	os.remove(x)
