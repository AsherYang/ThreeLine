package com.asher.threeline.ui.view;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Rect;
import android.os.Handler;
import android.util.AttributeSet;
import android.widget.TextView;

import uk.co.chrisjenx.calligraphy.TypefaceUtils;

/**
 * Created by ouyangfan on 17/6/4.
 * <p>
 * vertical text view
 */
public class VerticalTextView extends TextView {

    private Rect textBounds = new Rect();
    private Paint mPaint;
    private Path path = new Path();
    public static final int LAYOUT_CHANGED = 1;
    private static final int mTextLineSpace = 10;  // 列文本间距
    private int mTextPosx = 0;// x坐标
    private int mTextPosy = 0;// y坐标
    private int mTextWidth = 0;// 绘制宽度
    private int mTextHeight = 0;// 绘制高度
    private int mFontHeight = 0;// 绘制字体高度
    private float mFontSize = 24;// 字体大小
    private int mRealLine = 0;// 字符串真实的行数
    private int mLineWidth = 0;//列宽度
    private int mTextLength = 0;//字符串长度
    private int oldwidth = 0;//存储久的width
    private String text = "";//待显示的文字
    private Handler mHandler = null;
    private Matrix matrix;
    private Paint.Align textStartAlign = Paint.Align.RIGHT;//draw start left or right.//default right

    public VerticalTextView(Context context) {
        this(context, null);
    }

    public VerticalTextView(Context context, AttributeSet attrs) {
        this(context, attrs, 0);
    }

    public VerticalTextView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);

        initAttr(context, attrs);
    }

    private void initAttr(Context context, AttributeSet attrs) {
        mPaint = new Paint();
        matrix = new Matrix();
        mPaint.setTextAlign(Paint.Align.CENTER);//文字居中
        mPaint.setAntiAlias(true);//平滑处理
        mPaint.setColor(Color.BLACK);//默认文字颜色
        try {
            mFontSize = Float.parseFloat(attrs.getAttributeValue(null, "textSize"));//获取字体大小属性
        } catch (Exception e) {
        }
        setTypeface(TypefaceUtils.load(context.getAssets(), "fonts/jianshi_default.otf"));
    }

    public void setText(String text) {
        this.text = text;
        this.mTextLength = text.length();
        mPaint.getTextBounds(text, 0, text.length(), textBounds);
        if (mTextHeight > 0) {
            getTextInfo();
        }
    }

    //设置字体颜色
    public final void setTextColor(int color) {
        mPaint.setColor(color);
    }

    //设置字体大小
    public final void setTextSize(float size) {
        if (size != mPaint.getTextSize()) {
            mFontSize = size;
            if (mTextHeight > 0) {
                getTextInfo();
            }
        }
    }

    //设置行宽
    public void setLineWidth(int LineWidth) {
        mLineWidth = LineWidth;
    }

    //获取实际宽度
    public int getTextWidth() {
        return mTextWidth;
    }

    //计算文字行数和总宽
    private void getTextInfo() {
        char ch;
        int h = 0;
        mPaint.setTextSize(mFontSize);
        //获得字宽
        if (mLineWidth == 0) {
            float[] widths = new float[1];
            mPaint.getTextWidths("正", widths);//获取单个汉字的宽度
            mLineWidth = (int) Math.ceil(widths[0] * 1.1 + 2);
        }

        Paint.FontMetrics fm = mPaint.getFontMetrics();
        mFontHeight = (int) (Math.ceil(fm.descent - fm.top) * 0.9);// 获得字体高度

        //计算文字行数
        mRealLine = 0;
        for (int i = 0; i < this.mTextLength; i++) {
            ch = this.text.charAt(i);
            if (ch == '\n') {
                mRealLine++;// 真实的行数加一
                h = 0;
            } else {
                h += mFontHeight;
                if (h > this.mTextHeight) {
                    mRealLine++;// 真实的行数加一
                    i--;
                    h = 0;
                } else {
                    if (i == this.mTextLength - 1) {
                        mRealLine++;// 真实的行数加一
                    }
                }
            }
        }
        mRealLine++;//额外增加一行
        mTextWidth = (mLineWidth + mTextLineSpace) * mRealLine;//计算文字总宽度
        measure(mTextWidth, getHeight());//重新调整大小
        layout(getLeft(), getTop(), getLeft() + mTextWidth, getBottom());//重新绘制容器
    }

    //设置Handler，用以发送事件
    public void setHandler(Handler handler) {
        mHandler = handler;
    }

    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        int measuredWidth = measureWidth(widthMeasureSpec);
        int measuredHeight = measureHeight(heightMeasureSpec);
        if (mTextWidth == 0) {
            getTextInfo();
        }
        setMeasuredDimension(mTextWidth, measuredHeight);
        if (oldwidth != getWidth()) {
            oldwidth = getWidth();
            if (mHandler != null) mHandler.sendEmptyMessage(LAYOUT_CHANGED);
        }
    }

    private int measureWidth(int measureSpec) {
        int result = textBounds.width();
        int specMode = MeasureSpec.getMode(measureSpec);
        int specSize = MeasureSpec.getSize(measureSpec);

        if (specMode == MeasureSpec.EXACTLY) {
            result = specSize;
        } else if (specMode == MeasureSpec.AT_MOST) {
            result = specSize;
        }
        return result;
    }

    private int measureHeight(int measureSpec) {
        int result = textBounds.width();
        int specMode = MeasureSpec.getMode(measureSpec);
        int specSize = MeasureSpec.getSize(measureSpec);

        if (specMode == MeasureSpec.EXACTLY) {
            result = specSize;
        } else if (specMode == MeasureSpec.AT_MOST) {
            result = Math.min(result, specSize);
        }
        // 设置文本高度
        mTextHeight = result;
        return result;
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        draw(canvas, this.text);
    }

    private void draw(Canvas canvas, String textStr) {
        char ch;
        mTextPosy = 0;//初始化y坐标
        mTextPosx = textStartAlign == Paint.Align.LEFT ? mLineWidth : mTextWidth - mLineWidth;//初始化x坐标
        for (int i = 0; i < this.mTextLength; i++) {
            ch = textStr.charAt(i);
            if (ch == '\n') {
                if (textStartAlign == Paint.Align.LEFT) {
                    mTextPosx = mTextPosx + mLineWidth + mTextLineSpace;// 换列
                } else {
                    mTextPosx = mTextPosx - mLineWidth - mTextLineSpace;// 换列
                }
                mTextPosy = 0;
            } else if (ch == '《') {
                int startX = mTextPosx - 8;
                int startY = mTextPosy;
                int stopX = mTextPosx - 8;
                int stopY = mTextPosy + mFontHeight;
                path.moveTo(startX, startY);
                path.lineTo(stopX, stopY);
                mTextPosy += mFontHeight;
                canvas.drawTextOnPath(String.valueOf(ch), path, 0, 0, mPaint);
                path.reset();
            } else if (ch == '》') {
                int startX = mTextPosx - 8;
                int startY = mTextPosy + 10;
                int stopX = mTextPosx - 8;
                int stopY = mTextPosy + mFontHeight + 10;
                path.moveTo(startX, startY);
                path.lineTo(stopX, stopY);
                mTextPosy += mFontHeight + 10;
                canvas.drawTextOnPath(String.valueOf(ch), path, 0, 0, mPaint);
                path.reset();
            } else {
                mTextPosy += mFontHeight;
                if (mTextPosy > this.mTextHeight) {
                    if (textStartAlign == Paint.Align.LEFT) {
                        mTextPosx = mTextPosx + mLineWidth + mTextLineSpace;// 换列
                    } else {
                        mTextPosx = mTextPosx - mLineWidth - mTextLineSpace;// 换列
                    }
                    i--;
                    mTextPosy = 0;
                } else {
                    canvas.drawText(String.valueOf(ch), mTextPosx, mTextPosy, mPaint);
                }
            }
        }
    }
}
