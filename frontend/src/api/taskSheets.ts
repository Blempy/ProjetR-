import api from "./client";

export interface TaskSheetPayload {
  phase: string;
  task_name: string;
  responsable?: string;
  frequency?: string;
  duration?: string;
  objective: string;
  trigger?: string;
  steps?: string[];
  data_needed?: string[];
  docs_needed?: string[];
  tools_needed?: string[];
  outputs?: string[];
  formats?: string[];
  recipients?: string[];
  pains?: string[];
  automation_ideas?: string[];
  automation_type?: string;
  automation_prereq?: string;
  automation_effort?: string;
  automation_benefits?: string[];
  priority?: string;
  status?: string;
  next_action?: string;
  linked_docs?: string[];
}

export interface TaskSheetResponse {
  path: string;
  task_name: string;
  phase: string;
}

export async function createTaskSheet(payload: TaskSheetPayload): Promise<TaskSheetResponse> {
  const { data } = await api.post<TaskSheetResponse>("/staff/task-sheets", payload);
  return data;
}
