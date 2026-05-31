import { describe, expect, it } from "vitest";

function makerereGrade(mark) {
  const numericMark = Number(mark);
  if (!numericMark) return "Pending";
  if (numericMark >= 90) return "A+";
  if (numericMark >= 80) return "A";
  if (numericMark >= 75) return "B+";
  if (numericMark >= 70) return "B";
  if (numericMark >= 65) return "C+";
  if (numericMark >= 60) return "C";
  if (numericMark >= 55) return "D+";
  if (numericMark >= 50) return "D";
  if (numericMark >= 45) return "E";
  if (numericMark >= 40) return "E-";
  return "F";
}

function calculateTotal(evaluation) {
  return (
    Number(evaluation.technical || 0) +
    Number(evaluation.communication || 0) +
    Number(evaluation.attendance || 0)
  );
}

describe("grading helpers", () => {
  it("maps Makerere marks to letter grades", () => {
    expect(makerereGrade(92)).toBe("A+");
    expect(makerereGrade(85)).toBe("A");
    expect(makerereGrade(55)).toBe("D+");
    expect(makerereGrade(0)).toBe("Pending");
  });

  it("sums academic evaluation scores", () => {
    expect(
      calculateTotal({
        technical: 80,
        communication: 70,
        attendance: 90,
      }),
    ).toBe(240);
  });
});
