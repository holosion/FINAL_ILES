import { describe, expect, it } from "vitest";
import { modules, roles, workflowStates } from "../data/courseData";

describe("courseData", () => {
  it("lists all seven ILES modules required by CSC 1202", () => {
    expect(modules).toHaveLength(7);
    expect(modules).toContain("User & Role Management");
    expect(modules).toContain("Weighted Score Computation");
  });

  it("defines four role-based workflow participants", () => {
    expect(roles).toHaveLength(4);
    expect(roles.map((role) => role.name)).toEqual([
      "Student Intern",
      "Workplace Supervisor",
      "Academic Supervisor",
      "Internship Administrator",
    ]);
  });

  it("tracks the supervisor review workflow states", () => {
    expect(workflowStates.map((state) => state.key)).toEqual([
      "Draft",
      "Submitted",
      "Reviewed",
      "Approved",
    ]);
  });
});
