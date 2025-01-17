import React from "react";
import { GanttItem } from "components/gantt/types";
import { ETCaption2 } from "components/shared";
import { Palette } from "styles/theme";
import { Grid } from "@mui/material";
import { dateUtils } from "utils";
import { MONTH_DAY_YEAR } from "constants/application-constant";
import { getTaskSpan } from "../util";

export const CompletedPhase = ({ task }: { task: GanttItem }) => {
  const { formatDate } = dateUtils;
  const taskSpan = getTaskSpan(task.start, task.end);

  return (
    <Grid container alignItems={"flex-start"} textAlign={"left"}>
      <Grid
        item
        xs={12}
        sx={{
          backgroundColor: Palette.neutral.bg.light,
          borderBottom: `1px solid ${Palette.neutral.bg.dark}`,
          padding: "16px",
        }}
        justifyContent={"center"}
      >
        <ETCaption2 bold>{task.rowName}</ETCaption2>
      </Grid>
      <Grid
        item
        container
        alignItems="flex-start"
        justifyContent={"center"}
        spacing={2}
        sx={{
          padding: "16px",
        }}
      >
        <Grid item xs={12}>
          <ETCaption2
            sx={{
              flex: 1,
              width: "100%",
            }}
            bold
          >
            {task.name}
          </ETCaption2>
        </Grid>
        <Grid item xs={12} container alignItems="flex-start" spacing={1}>
          <Grid item xs={12} container alignItems="flex-start">
            <Grid item xs={6}>
              <ETCaption2>Phase Start:</ETCaption2>
            </Grid>
            <Grid item xs={6}>
              <ETCaption2>
                {formatDate(task.start.toDateString(), MONTH_DAY_YEAR)}
              </ETCaption2>
            </Grid>
          </Grid>
          <Grid item xs={12} container alignItems="flex-start">
            <Grid item xs={6}>
              <ETCaption2>Phase End:</ETCaption2>
            </Grid>
            <Grid item xs={6}>
              <ETCaption2>
                {formatDate(task.end.toDateString(), MONTH_DAY_YEAR)}
              </ETCaption2>
            </Grid>
          </Grid>

          <Grid item xs={12} container alignItems="flex-start">
            <Grid item xs={6}>
              <ETCaption2>Days:</ETCaption2>
            </Grid>
            <Grid item xs={6}>
              <ETCaption2>{taskSpan}</ETCaption2>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
};
