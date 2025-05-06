import { UserConfig } from "@commitlint/types";

const configuration: UserConfig = {
  extends: ["@commitlint/config-conventional"],
  formatter: "@commitlint/format",
  ignores: [(message) => message.startsWith("chore(release):")],
};

export default configuration;
