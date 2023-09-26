export enum EVENT_STATUS {
  NOT_STARTED = "NOT_STARTED",
  INPROGRESS = "INPROGRESS",
  COMPLETED = "COMPLETED",
}
export const statusOptions = [
  {
    label: "Not Started",
    value: EVENT_STATUS.NOT_STARTED,
  },
  {
    label: "In Progress",
    value: EVENT_STATUS.INPROGRESS,
  },
  {
    label: "Complete",
    value: EVENT_STATUS.COMPLETED,
  },
];
export interface TaskEvent {
  id: number;
  name: string;
  work_id: number;
  phase_id: number;
  responsibility_id: number;
  start_date: string;
  number_of_days: number;
  tips: string;
  notes: string;
  assignee_ids?: string[];
  status: EVENT_STATUS;
}