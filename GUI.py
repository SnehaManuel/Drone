<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>794</width>
    <height>496</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>-10</x>
     <y>0</y>
     <width>811</width>
     <height>501</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">Qlabel{
background-image: url(:/rec/tuse.png);
}</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap resource="rec.qrc">:/rec/tuse.png</pixmap>
   </property>
   <property name="scaledContents">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>160</y>
     <width>341</width>
     <height>211</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap resource="rec.qrc">:/rec/gifloader.gif</pixmap>
   </property>
   <property name="scaledContents">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="label_4">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>150</y>
     <width>81</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:12pt; color:#ffffff;&quot;&gt;24 JULY 2022&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QPushButton" name="RUN">
   <property name="geometry">
    <rect>
     <x>710</x>
     <y>40</y>
     <width>71</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>8514oem</family>
     <pointsize>16</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(0, 0, 127);
background-color: rgb(0, 0, 255);</string>
   </property>
   <property name="text">
    <string>RUN</string>
   </property>
  </widget>
  <widget class="QPushButton" name="EXIT">
   <property name="geometry">
    <rect>
     <x>710</x>
     <y>90</y>
     <width>71</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>8514oem</family>
     <pointsize>16</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(0, 0, 255);</string>
   </property>
   <property name="text">
    <string>EXIT</string>
   </property>
  </widget>
 </widget>
 <resources>
  <include location="rec.qrc"/>
 </resources>
 <connections/>
</ui>
