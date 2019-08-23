import re
import sys
import json
from os.path import dirname, join
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler, intent_file_handler
from mycroft.messagebus.message import Message
from mycroft.skills.core import resting_screen_handler

class SkillGuiExample(MycroftSkill):
    """
    Example Skill Showcasing All Delegates
    """

    def __init__(self):
        super().__init__("SkillGuiExample")
        self.html_resources = "file://" + dirname(__file__) + '/res/'

    def initialize(self):
        # Handle Menu and Navigation
        self.gui.register_handler('SkillGuiExample.simpleText',
                                  self.handle_gui_example_simpleText_intent)
        self.gui.register_handler('SkillGuiExample.simpleImage',
                                  self.handle_gui_example_simpleImage_intent)
        self.gui.register_handler('SkillGuiExample.paginatedText',
                                  self.handle_gui_example_paginatedText_intent)
        self.gui.register_handler('SkillGuiExample.slidingImage',
                                  self.handle_gui_example_slidingImage_intent)
        self.gui.register_handler(
            'SkillGuiExample.proportionalDelegate',
            self.handle_gui_example_proportionalDelegate_intent)
        self.gui.register_handler(
            'SkillGuiExample.proportionalDelegateWrapText',
            self.handle_gui_example_proportionalDelegateWrapText_intent)
        self.gui.register_handler('SkillGuiExample.listView',
                                  self.handle_gui_example_listView_intent)
        self.gui.register_handler('SkillGuiExample.eventsExample',
                                  self.handle_gui_example_events_intent)
        self.gui.register_handler('SkillGuiExample.audioDelegateExample',
                                  self.handle_gui_example_audioDelegate_intent)
        self.gui.register_handler('SkillGuiExample.htmlUrlExample', 
                                  self.handle_gui_example_showHTMLUrl_intent)
        self.gui.register_handler('SkillGuiExample.htmlRawExample', 
                                  self.handle_gui_example_showHTMLRaw_intent)
        self.gui.register_handler('SkillGuiExample.videoExample', 
                                  self.handle_gui_example_showVideo_intent)
        self.gui.register_handler('SkillGuiExample.menu',
                                  self.handle_gui_example_menu_intent)

        # Handle example events
        self.gui.register_handler('SkillGuiExample.colorChange',
                                  self.change_color_event)

    @intent_handler(IntentBuilder('handle_gui_example_simpleText_intent').require('gui.example.one'))
    def handle_gui_example_simpleText_intent(self, message):
        """
        Example Intent Showcasing Basic UI Text
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui.show_text("Lorem ipsum dolor sit amet booom baka kakakaka.")

    @intent_handler(IntentBuilder('handle_gui_example_simpleImage_intent').require('gui.example.two'))
    def handle_gui_example_simpleImage_intent(self, message):
        """
        Example Intent Showcasing Basic UI Image
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui.show_image("https://source.unsplash.com/1920x1080/?+random", "Example Long Caption That Needs Wrapping Very Long Long Text Text Example That Is", "Example Title")

    @intent_handler(IntentBuilder('handle_gui_example_paginatedText_intent').require('gui.example.three'))
    def handle_gui_example_paginatedText_intent(self, message):
        """
        Example Intent Showcasing Paginated UI Text
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui['sampleText'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Aliquam sem et tortor consequat id porta nibh. Amet est placerat in egestas erat imperdiet sed. Ut ornare lectus sit amet est placerat in egestas erat. Iaculis eu non diam phasellus vestibulum lorem sed risus ultricies. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Vulputate eu scelerisque felis imperdiet proin fermentum. Neque convallis a cras semper auctor neque. Pharetra magna ac placerat vestibulum lectus mauris ultrices eros in. Phasellus faucibus scelerisque eleifend donec pretium vulputate. Malesuada bibendum arcu vitae elementum curabitur vitae nunc. Tellus id interdum velit laoreet id donec. Diam donec adipiscing tristique risus nec. Nisi lacus sed viverra tellus in hac habitasse platea. Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Sit amet nisl suscipit adipiscing bibendum est ultricies. Nec ultrices dui sapien eget mi proin sed. Egestas dui id ornare arcu odio ut sem nulla. Rhoncus aenean vel elit scelerisque. Neque gravida in fermentum et sollicitudin. Pellentesque massa placerat duis ultricies lacus sed. Nunc id cursus metus aliquam eleifend mi. Eu feugiat pretium nibh ipsum consequat nisl. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae. Est ante in nibh mauris cursus mattis. Sagittis eu volutpat odio facilisis mauris sit amet. At consectetur lorem donec massa sapien faucibus. Odio facilisis mauris sit amet. Quis ipsum suspendisse ultrices gravida dictum fusce. Sagittis nisl rhoncus mattis rhoncus urna neque viverra justo nec. Eget mi proin sed libero enim sed faucibus. Interdum velit euismod in pellentesque massa. Et netus et malesuada fames. Velit aliquet sagittis id consectetur purus. Condimentum lacinia quis vel eros donec ac odio tempor orci. Amet consectetur adipiscing elit pellentesque habitant. Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Nisi porta lorem mollis aliquam ut porttitor leo a diam. Egestas integer eget aliquet nibh praesent tristique. Velit scelerisque in dictum non. Id volutpat lacus laoreet non curabitur gravida arcu ac. Suspendisse interdum consectetur libero id faucibus nisl tincidunt eget. Ipsum a arcu cursus vitae congue mauris. Duis at consectetur lorem donec massa. Orci sagittis eu volutpat odio facilisis mauris. Eget mauris pharetra et ultrices neque ornare. Commodo nulla facilisi nullam vehicula ipsum a. Arcu risus quis varius quam quisque. Gravida in fermentum et sollicitudin. Lacus laoreet non curabitur gravida arcu ac tortor dignissim. Netus et malesuada fames ac turpis. Ipsum dolor sit amet consectetur adipiscing. Tellus elementum sagittis vitae et leo duis ut diam quam. Vitae et leo duis ut diam quam nulla. Risus pretium quam vulputate dignissim. Justo laoreet sit amet cursus sit amet dictum sit. Blandit libero volutpat sed cras. Lacus sed viverra tellus in. Ornare lectus sit amet est placerat in egestas erat. Tortor dignissim convallis aenean et tortor at. Tempus quam pellentesque nec nam aliquam. Nisi scelerisque eu ultrices vitae auctor eu augue ut lectus. Consequat id porta nibh venenatis cras sed felis eget. Massa enim nec dui nunc mattis enim ut. Dignissim enim sit amet venenatis urna. Ac tincidunt vitae semper quis lectus nulla at. Sed felis eget velit aliquet sagittis. Vel turpis nunc eget lorem dolor sed viverra. Non consectetur a erat nam at lectus. Iaculis eu non diam phasellus vestibulum. Dolor sit amet consectetur adipiscing elit ut aliquam purus sit. Libero justo laoreet sit amet cursus sit. Tellus pellentesque eu tincidunt tortor. Maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Semper risus in hendrerit gravida rutrum quisque non tellus orci. Diam in arcu cursus euismod quis viverra nibh cras pulvinar. Habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat. Elit ut aliquam purus sit."
        self.gui.show_page("paginationExample.qml")

    @intent_handler(IntentBuilder('handle_gui_example_slidingImage_intent').require('gui.example.four'))
    def handle_gui_example_slidingImage_intent(self, message):
        """
        Example Intent Showcasing Sliding Image UI
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui['sampleImage'] = "https://source.unsplash.com/1920x1080/?+random"
        self.gui.show_page("slidingExample.qml")

    @intent_handler(IntentBuilder('handle_gui_example_proportionalDelegate_intent').require('gui.example.five'))
    def handle_gui_example_proportionalDelegate_intent(self, message):
        """
        Example Intent Showcasing Proportional Delegate and Autofit Label
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui['sampleText'] = "Loading.."
        self.gui.show_page("proportionalDelegateExample.qml")

    @intent_handler(IntentBuilder('handle_gui_example_proportionalDelegateWrapText_intent').require('gui.example.five.wrapText'))
    def handle_gui_example_proportionalDelegateWrapText_intent(self, message):
        """
        Example Intent Showcasing Proportional Delegate and Autofit Label
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui['sampleText'] = "Incomprehensibilities"
        self.gui.show_page("proportionalDelegateWrapExample.qml")

    @intent_handler(IntentBuilder('handle_gui_example_listView_intent').require('gui.example.six'))
    def handle_gui_example_listView_intent(self, message):
        """
        Example Intent Showcasing Advanced QML Skills with List and JSON Models
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        sampleObject = {}
        sampleList = [{"text": "Praesent id leo felis",
                       "image": "https://c1.staticflickr.com/8/7246/13792463963_817450e973_b.jpg"},
                      {"text": "Cras egestas tempus tempus",
                       "image": "https://c1.staticflickr.com/8/7246/13792463963_817450e973_b.jpg"},
                      {"text": "Habitasse platea dictumst",
                       "image": "https://c1.staticflickr.com/8/7246/13792463963_817450e973_b.jpg"}]
        sampleObject['lorem'] = sampleList
        self.gui['sampleBlob'] = sampleObject
        self.gui['background'] = "https://source.unsplash.com/1920x1080/?+random"
        self.gui.show_page("listViewExample.qml")

    @intent_handler(IntentBuilder('handle_gui_example_events_intent').require('gui.example.seven'))
    def handle_gui_example_events_intent(self, message):
        """
        Example Intent Showcasing Events Between Skill and Display
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui.show_page("eventsExample.qml")

    def change_color_event(self, message):
        """
        Change Color Event
        """
        self.gui['fooColor'] = message.data['color']
        self.gui.show_page("eventsExample.qml")

    @intent_handler(IntentBuilder('handle_gui_example_audioDelegate_intent').require('gui.example.eight'))
    def handle_gui_example_audioDelegate_intent(self, message):
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui["audioSource"] = "https://www.free-stock-music.com/music/serge-narcissoff-background-theme.mp3"
        self.gui["audioTitle"] = "Background Theme by Serge Narcissoff "
        self.gui["audioThumb"] = "https://www.free-stock-music.com/thumbnails/serge-narcissoff-background-theme.jpg"
        self.gui.show_page("audioPlayerExample.qml")
        
    @intent_handler(IntentBuilder('handle_gui_example_showHTMLUrl_intent').require('gui.example.nine'))
    def handle_gui_example_showHTMLUrl_intent(self, message):
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui.show_url("https://mycroft.ai/", override_idle=True)

    @intent_handler(IntentBuilder('handle_gui_example_showHTMLRaw_intent').require('gui.example.ten'))
    def handle_gui_example_showHTMLRaw_intent(self, message):
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        rawhtmlexample = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
<body>
<h1> HTML Example </h1>
<img src="apple.png" width=150px height=100px>
<p> This is an example of an HTML webpage. </p>
<p> <b>Tags</b> can be wrapped <i>inside other tags!</i> </p>

<p>
	HTML doesn't care about extra spaces, tabs or newlines,
	so we can use indentation and spacing to keep everything
	lined up nicely.
</p>

<ul>
	<li> This is how you create a bulleted list! </li>
	<li> Item 2 </li>
	<li> Item 3 </li>
</ul>
</body>
</html>
"""
        self.gui.show_html(rawhtmlexample, resource_url=self.html_resources, override_idle=True)
        
        
    @intent_handler(IntentBuilder('handle_gui_video_example_intent').require('gui.example.eleven'))
    def handle_gui_example_showVideo_intent(self, message):
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui["video"] = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"
        self.gui["status"] = "play"
        self.gui.show_page("videoPlayerExample.qml")
        
    @intent_handler(IntentBuilder('handle_gui_example_menu_intent').require('gui.example.menu'))
    def handle_gui_example_menu_intent(self, message):
        """
        Build and Show Skill Example Menu To Run Test
        """
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        menuObject = {}
        menuList = [{
            "exampleIcon": "beamerblock",
            "exampleLabel": "Simple Text Example",
            "exampleEvent": "SkillGuiExample.simpleText"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Simple Image Example",
            "exampleEvent": "SkillGuiExample.simpleImage"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Paginated Text Example",
            "exampleEvent": "SkillGuiExample.paginatedText"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Sliding Image Example",
            "exampleEvent": "SkillGuiExample.slidingImage"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Proportion Delegate & Autofit Label",
            "exampleEvent": "SkillGuiExample.proportionalDelegate"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Proportion Delegate Word Wrap",
            "exampleEvent": "SkillGuiExample.proportionalDelegateWrapText"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Cards ListView",
            "exampleEvent": "SkillGuiExample.listView"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Events Example",
            "exampleEvent": "SkillGuiExample.eventsExample"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Audio Player Example",
            "exampleEvent": "SkillGuiExample.audioDelegateExample"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Html Url Example",
            "exampleEvent": "SkillGuiExample.htmlUrlExample"
        },
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Html Raw Example",
            "exampleEvent": "SkillGuiExample.htmlRawExample"
        },            
            {
            "exampleIcon": "beamerblock",
            "exampleLabel": "Video Player Example",
            "exampleEvent": "SkillGuiExample.videoExample"
        }]
        menuObject['menuItems'] = menuList
        self.gui['menuBlob'] = menuObject
        self.gui.show_page("exampleMenu.qml")

    @resting_screen_handler('Example Idle')
    def handle_idle(self, message):
        self.gui.clear()
        self.log.info('Activating foo/bar resting page')
        self.gui["exampleText"] = "This Is A Idle Screen"
        self.gui.show_page('idle.qml')

    def stop(self):
        pass


def create_skill():
    return SkillGuiExample()
