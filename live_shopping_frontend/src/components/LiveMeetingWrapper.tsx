import { DyteProvider, useDyteClient } from "@dytesdk/react-web-core";
import React, { useEffect } from "react";
import { getUserToken, startLiveVideoRequest } from "../api/backend";
import { provideDyteDesignSystem } from "@dytesdk/react-ui-kit";
import CustomDyteMeeting from "./DyteMeeting";
interface LiveMeetingWrapperProps {
  id: number;
  type: "user" | "support";
  dyte_auth_token?: string
}
const LiveMeetingWrapper: React.FC<LiveMeetingWrapperProps> = ({ id, type, dyte_auth_token }) => {
  const [meeting, initMeeting] = useDyteClient();
  const getDyteAuthToken = async (): Promise<string> => {
    if (type === 'user') {
      const auth_token = await getUserToken(id);
      return auth_token.dyte_auth_token
    } else {
      const auth_token = await startLiveVideoRequest(id)
      return auth_token.dyte_auth_token
    }
  }
  const onRoomLeft = () => {
    // Event handler to run on leaving the meeting.
  }
  const setupDyteMeeting = async () => {
    if (!dyte_auth_token) {
      dyte_auth_token = await getDyteAuthToken();
    }
    await initMeeting({
      authToken: dyte_auth_token,
      defaults: {
        audio: false,
        video: false
      }
    })
  }
  useEffect(() => {
    setupDyteMeeting();
  }, [])
  
  useEffect(() => {
    provideDyteDesignSystem(document.body, {
      theme: 'light',
    });
  }, []);
  
  useEffect(() => {
    if(meeting) {
      meeting.joinRoom();
      meeting.self.on('roomLeft', onRoomLeft);
      return () => {
          meeting.self.removeListener('roomLeft', onRoomLeft);
      }
  }}, [meeting]);
  
  return (
    <DyteProvider value={meeting} fallback={<div>Loading...</div>}>
        <CustomDyteMeeting onRoomLeft={onRoomLeft}/>
    </DyteProvider>
  )
}
export default LiveMeetingWrapper;