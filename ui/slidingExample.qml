import QtQuick 2.4
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.4
import org.kde.kirigami 2.4 as Kirigami
import Mycroft 1.0 as Mycroft

Mycroft.Delegate {
     background: Mycroft.SlidingImage {
     id: slidingImage
     source: sessionData.sampleImage
     running: false
     speed: 0.2         //Animation speed in Kirigami.Units.gridUnit / second
     onSourceChanged: {
         slidingImage.running = true
        }
    }
   
    RoundButton {
        id: backButton
        anchors.top: parent.top
        anchors.left: parent.left
        implicitWidth: Kirigami.Units.iconSizes.medium
        implicitHeight: implicitWidth
        icon.name: "go-previous-symbolic"
        onClicked: {
            triggerGuiEvent("SkillGuiExample.menu", {})
        }
    }
} 
