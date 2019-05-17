import QtQuick 2.4
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.4
import org.kde.kirigami 2.4 as Kirigami
import Mycroft 1.0 as Mycroft
import org.kde.lottie 1.0

Mycroft.ProportionalDelegate {
    id: root
    skillBackgroundColorOverlay: "#000000"

    Mycroft.AutoFitLabel {
        id: exampleLabel
        Layout.fillWidth: true
        Layout.preferredHeight: proportionalGridUnit * 30
        wrapMode: Text.Wrap
        font.family: "Noto Sans"
        font.weight: Font.Bold
        text: sessionData.sampleText
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
