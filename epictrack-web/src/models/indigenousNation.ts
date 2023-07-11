import { ListType } from "./code";
import { Staff } from "./staff";
import { MasterBase } from "./type";

export interface IndigenousNation extends ListType, MasterBase {
    is_active: boolean,
    relationship_holder_id?: number,
    relationship_holder?: Staff
}