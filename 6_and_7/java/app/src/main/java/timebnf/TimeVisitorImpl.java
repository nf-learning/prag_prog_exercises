package timebnf;
// TODO Implement getMinutesAfterMidnight()

public class TimeVisitorImpl extends TimeBaseVisitor<Integer> {

    @Override
    public Integer visitTime(TimeParser.TimeContext ctx) {
        System.out.println(ctx.getText());
        return super.visitTime(ctx);
    }

    @Override
    public Integer visitHour(TimeParser.HourContext ctx) {
        System.out.println(ctx.getText());
        return super.visitHour(ctx);
    }

    @Override
    public Integer visitMinute(TimeParser.MinuteContext ctx) {
        System.out.println(ctx.getText());
        return super.visitMinute(ctx);
    }
}
