package com.asher.threeline.ui.view;

import android.app.Activity;
import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Color;
import android.text.TextUtils;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.asher.threeline.R;

/**
 * Created by ouyangfan on 17/5/9.
 * <p>
 * titleBar
 * 沉浸式状态栏
 */
public class TitleBar extends LinearLayout {

    // TODO: 17/5/10 add textSize
    private int statusBarColor;
    private int titleBarColor;
    private int titleBarTextColor;
    private float titleBarTitleHeight;
    private String titleBarTitle;

    private TextView leftText;
    private ImageView leftImage;
    private TextView centerText;
    private TextView rightText;
    private ImageView rightImage;

    public static final int NO_RES_ID = -1;

    public TitleBar(Context context) {
        this(context, null);
    }

    public TitleBar(Context context, AttributeSet attrs) {
        this(context, attrs, 0);
    }

    public TitleBar(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init(context, attrs);
    }

    private void init(Context context, AttributeSet attrs) {
        //获取属性值
        TypedArray a = context.obtainStyledAttributes(attrs, R.styleable.TitleBar);
        statusBarColor = a.getColor(R.styleable.TitleBar_statusBarColor, getResources().getColor(R.color.colorPrimary));
        titleBarColor = a.getColor(R.styleable.TitleBar_titleBarColor, getResources().getColor(R.color.colorPrimaryDark));
        titleBarTextColor = a.getColor(R.styleable.TitleBar_titleBarTextColor, Color.WHITE);
        titleBarTitleHeight = a.getDimension(R.styleable.TitleBar_titleBarTitleHeight, getResources().getDimension(R.dimen.defalut_titlebar_height));
        titleBarTitle = a.getString(R.styleable.TitleBar_titleBarTitle);
        a.recycle();

        // 设置沉浸式statusBar，以及颜色
        setFitsSystemWindows(true);
        setClipToPadding(true);
        setOrientation(VERTICAL);
        setBackgroundColor(statusBarColor);

        ViewGroup.LayoutParams title_lp = new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,
                (int) titleBarTitleHeight);

        View titleBarView = LayoutInflater.from(context).inflate(R.layout.layout_title_bar, null, false);
        titleBarView.setBackgroundColor(titleBarColor);
        leftText = (TextView) titleBarView.findViewById(R.id.left_text);
        leftImage = (ImageView) titleBarView.findViewById(R.id.left_image);
        centerText = (TextView) titleBarView.findViewById(R.id.center_text);
        rightText = (TextView) titleBarView.findViewById(R.id.right_text);
        rightImage = (ImageView) titleBarView.findViewById(R.id.right_image);

        leftText.setTextColor(titleBarTextColor);
        rightText.setTextColor(titleBarTextColor);
        centerText.setTextColor(titleBarTextColor);
        centerText.setText(titleBarTitle);

        addView(titleBarView, title_lp);
    }

    public TextView getLeftText() {
        return leftText;
    }

    public ImageView getLeftImage() {
        return leftImage;
    }

    public TextView getCenterText() {
        return centerText;
    }

    public TextView getRightText() {
        return rightText;
    }

    public ImageView getRightImage() {
        return rightImage;
    }

    /**
     * 只显示标题
     *
     * @param title
     */
    public void setTitleBar(String title) {
        setTitleBar(title, null, null, NO_RES_ID, NO_RES_ID);
    }

    /**
     * 标题加返回
     *
     * @param title
     */
    public void setTitleBarWithBack(String title) {
        setTitleBar(title, null, null, R.drawable.title_bar_left_back, NO_RES_ID);
    }

    public void setTitleBar(String title, int leftResId, int rightResId) {
        setTitleBar(title, null, null, leftResId, rightResId);
    }

    public void setTitleBar(String title, String leftText, String rightText) {
        setTitleBar(title, leftText, rightText, NO_RES_ID, NO_RES_ID);
    }

    /**
     * 返回按钮+右边文字
     *
     * @param title
     * @param rightText
     */
    public void setTitleBar(String title, String rightText) {
        setTitleBar(title, null, rightText, NO_RES_ID, NO_RES_ID);
    }

    /**
     * 返回按钮+右边图标
     *
     * @param title
     * @param rightResId
     */
    public void setTitleBar(String title, int rightResId) {
        setTitleBar(title, null, null, NO_RES_ID, rightResId);
    }

    /**
     * 控制标题样式
     *
     * @param title
     * @param leftTitle  左侧按钮文字 不显示为null
     * @param rightTitle 右侧按钮文字 不显示为null
     * @param leftResId  左侧按钮图片 不显示为 {@link TitleBar#NO_RES_ID}
     * @param rightResId 右侧按钮图片 不显示为 {@link TitleBar#NO_RES_ID}
     */
    public void setTitleBar(String title, String leftTitle, String rightTitle, int leftResId, int rightResId) {


        //左标题文字为空,则不显示
        if (TextUtils.isEmpty(leftTitle)) {
            leftText.setVisibility(View.GONE);
        } else {
            leftText.setVisibility(View.VISIBLE);
            leftText.setText(leftTitle);
        }

        //右标题文字为空,则不显示
        if (TextUtils.isEmpty(leftTitle)) {
            rightText.setVisibility(View.GONE);
        } else {
            rightText.setVisibility(View.VISIBLE);
            rightText.setText(rightTitle);
        }

        if (leftResId != NO_RES_ID) {
            leftImage.setVisibility(View.VISIBLE);
            leftImage.setImageResource(leftResId);
        } else {
            leftImage.setVisibility(View.GONE);
        }

        if (rightResId != NO_RES_ID) {
            rightImage.setVisibility(View.VISIBLE);
            rightImage.setImageResource(rightResId);
        } else {
            rightImage.setVisibility(View.GONE);
        }

        if (!TextUtils.isEmpty(title)) {
            centerText.setVisibility(View.VISIBLE);
            centerText.setText(title);
        } else {
            centerText.setVisibility(View.GONE);
        }

    }


    /**
     * 左部按钮点击事件
     *
     * @param listener
     */
    public void setLeftOnClickListener(View.OnClickListener listener) {
        if (leftText.getVisibility() == View.VISIBLE) {
            leftText.setOnClickListener(listener);
        } else {
            leftImage.setOnClickListener(listener);
        }

    }


    /**
     * 右部按钮点击事件
     *
     * @param listener
     */
    public void setRightOnClickListener(View.OnClickListener listener) {
        if (rightText.getVisibility() == View.VISIBLE) {
            rightText.setOnClickListener(listener);
        } else {
            rightImage.setOnClickListener(listener);
        }
    }

    /**
     * 标题点击事件
     *
     * @param listener
     */
    public void setCenterOnClickListener(View.OnClickListener listener) {
        if (centerText.getVisibility() == View.VISIBLE) {
            centerText.setOnClickListener(listener);
        }
    }

    public static int getStatusBarHeight(Context context) {
        int result = 0;
        int resourceId = context.getResources().getIdentifier("status_bar_height", "dimen", "android");
        if (resourceId > 0) {
            result = context.getResources().getDimensionPixelSize(resourceId);
        }
        return result;
    }

    public static TitleBar getInstance(Activity context) {
        return (TitleBar) ((ViewGroup) context.findViewById(android.R.id.content)).getChildAt(0);
    }
}