package com.asher.threeline.ui.main;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;

import com.asher.threeline.R;

public class ImageAdapter extends BaseAdapter {

    private LayoutInflater mInflater;
    private static final int[] ids = {R.drawable.block_canary_icon, R.drawable.ic_launcher, R.drawable.block_canary_icon, R.drawable.ic_launcher,
            R.drawable.block_canary_icon, R.drawable.ic_launcher, R.drawable.next};

    public ImageAdapter(Context context) {
        mInflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
    }

    @Override
    public int getCount() {
        return ids.length;
    }

    @Override
    public Object getItem(int position) {
        return position;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.layout_music_item, null);
        }
        ((ImageView) convertView.findViewById(R.id.iv_music_cover)).setImageResource(ids[position]);
        ImageView musicPlay = (ImageView) convertView.findViewById(R.id.iv_music_play);
        musicPlay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });
        return convertView;
    }

}
