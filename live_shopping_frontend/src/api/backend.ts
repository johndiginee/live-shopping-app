import axios from 'axios';

const BASE_URL = 'http://localhost:3000';

export interface IProduct {
  id: number;
  title: string;
  rating: {rate: number},
  price: number,
  image?: URL
}

export interface CreateLiveVideoRequestData {
  user_name: string;
  user_email: string;
  product: IProduct;
}

export interface LiveVideoRequest {
  id: number;
  user_email: string;
  user_name: string;
  user_dyte_participant_id: string;
  support_user_dyte_participant_id: string | null;
  dyte_meeting_id: string;
  status: "PENDING" | "ACTIVE" | "DONE"
}

export const createLiveVideoRequest = async (
  data: CreateLiveVideoRequestData,
): Promise<LiveVideoRequest> => {
  const response = await axios.post(`${BASE_URL}/live-shopping/live-requests/`, data);
  return response.data;
};

export const listLiveVideoRequest = async (): Promise <LiveVideoRequest[]> => {
  const response = await axios.get(`${BASE_URL}/live-shopping/live-requests/`);
  return response.data;
}

export const startLiveVideoRequest = async(
  id: number
): Promise<{ dyte_auth_token: string }> => {
  const response = await axios.post(`${BASE_URL}/live-shopping/live-requests/${id}/start/`);
  return response.data
}

export const getUserToken = async(
  id: number
): Promise<{ dyte_auth_token: string }> => {
  const response = await axios.get(`${BASE_URL}/live-shoppong/live-request/${id}/user-token`);
  return response.data
}