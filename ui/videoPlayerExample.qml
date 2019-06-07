import QtQuick.Layouts 1.4
import QtQuick 2.9
import QtQuick.Controls 2.0 as Controls
import org.kde.kirigami 2.4 as Kirigami
import QtGraphicalEffects 1.0

import Mycroft 1.0 as Mycroft

Mycroft.Delegate {
    id: root
    fillWidth: true
    background: Rectangle {
        color: "black"
    }
    leftPadding: 0
    topPadding: 0
    rightPadding: 0
    bottomPadding: 0
    
    Mycroft.VideoPlayer {
        id: youtubePlayer
        anchors.fill: parent
        source: sessionData.video
        hasNextAction: false
        hasPreviousAction: false
        status: sessionData.status
    }
}
