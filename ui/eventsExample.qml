import QtQuick 2.4
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.4
import org.kde.kirigami 2.4 as Kirigami
import Mycroft 1.0 as Mycroft

Mycroft.Delegate {
    id: root
    property var rectColor: sessionData.fooColor

    onRectColorChanged: {
        fooRect.color = rectColor
    }

    Rectangle {
        id: fooRect
        anchors.fill: parent
        color: "#000"
        
        ColumnLayout {
            anchors.fill: parent
            
            Button {
                id: fooButton
                Layout.fillWidth: true
                height: Kirigami.Units.gridUnit * 2
                text: "blue"
                
                onClicked: {
                    triggerGuiEvent("SkillGuiExample.colorChange", {"color": "#0000ff"})
                }
            }
            Button {
                id: fooButton2
                Layout.fillWidth: true
                height: Kirigami.Units.gridUnit * 2
                text: "red"
                
                onClicked: {
                    triggerGuiEvent("SkillGuiExample.colorChange", {"color": "#ff0000"})
                }
            }
            Button {
                id: fooButton3
                Layout.fillWidth: true
                height: Kirigami.Units.gridUnit * 2
                text: "black"
                
                onClicked: {
                    triggerGuiEvent("SkillGuiExample.colorChange", {"color": "#000000"})
                }
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
}
